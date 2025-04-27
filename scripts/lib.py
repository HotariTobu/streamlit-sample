import streamlit as st
from typing import TypeVar, Callable

T = TypeVar("T")


class StateFactory:
    """A factory for creating Streamlit state variables with unique keys."""

    def __init__(self, key: str | None = None):
        self.key = "" if key is None else key
        self.count = 0

    def __call__(self, initial: T = None) -> tuple[T, Callable[[T], None]]:
        """Define a Streamlit state variable with a unique key.

        Args:
            initial (T, optional): The initial value of the state. Defaults to None.

        Returns:
            tuple[T, Callable[[T], None]]: [value, setter]: A tuple containing the current value of the state and a setter function to update it.
        """

        self.count += 1
        id = f"{self.key}-{self.count}"

        value = initial

        if id in st.session_state:
            value = st.session_state[id]
        else:
            st.session_state[id] = initial

        def setter(new_value: T) -> None:
            st.session_state[id] = new_value
            st.rerun()

        return value, setter
