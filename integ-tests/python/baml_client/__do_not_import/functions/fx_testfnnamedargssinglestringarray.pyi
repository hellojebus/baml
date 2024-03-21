# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from baml_core.stream import AsyncStream
from typing import Callable, List, Protocol, runtime_checkable


import typing

import pytest
from contextlib import contextmanager
from unittest import mock

ImplName = typing.Literal["v1"]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


ITestFnNamedArgsSingleStringArrayOutput = str

@runtime_checkable
class ITestFnNamedArgsSingleStringArray(Protocol):
    """
    This is the interface for a function.

    Args:
        myStringArray: List[str]

    Returns:
        str
    """

    async def __call__(self, *, myStringArray: List[str]) -> str:
        ...

   

@runtime_checkable
class ITestFnNamedArgsSingleStringArrayStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        myStringArray: List[str]

    Returns:
        AsyncStream[str, str]
    """

    def __call__(self, *, myStringArray: List[str]
) -> AsyncStream[str, str]:
        ...
class BAMLTestFnNamedArgsSingleStringArrayImpl:
    async def run(self, *, myStringArray: List[str]) -> str:
        ...
    
    def stream(self, *, myStringArray: List[str]
) -> AsyncStream[str, str]:
        ...

class IBAMLTestFnNamedArgsSingleStringArray:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[ITestFnNamedArgsSingleStringArray, ITestFnNamedArgsSingleStringArrayStream], None]:
        ...

    async def __call__(self, *, myStringArray: List[str]) -> str:
        ...

    def stream(self, *, myStringArray: List[str]
) -> AsyncStream[str, str]:
        ...

    def get_impl(self, name: ImplName) -> BAMLTestFnNamedArgsSingleStringArrayImpl:
        ...

    @contextmanager
    def mock(self) -> typing.Generator[mock.AsyncMock, None, None]:
        """
        Utility for mocking the TestFnNamedArgsSingleStringArrayInterface.

        Usage:
            ```python
            # All implementations are mocked.

            async def test_logic() -> None:
                with baml.TestFnNamedArgsSingleStringArray.mock() as mocked:
                    mocked.return_value = ...
                    result = await TestFnNamedArgsSingleStringArrayImpl(...)
                    assert mocked.called
            ```
        """
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the TestFnNamedArgsSingleStringArrayInterface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.TestFnNamedArgsSingleStringArray.test
            async def test_logic(TestFnNamedArgsSingleStringArrayImpl: ITestFnNamedArgsSingleStringArray) -> None:
                result = await TestFnNamedArgsSingleStringArrayImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName] = [], stream: bool = False) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the TestFnNamedArgsSingleStringArrayInterface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.
            stream: bool
                If set, will return a streamable version of the test function.

        Usage:
            ```python
            # All implementations except the given impl will be tested.

            @baml.TestFnNamedArgsSingleStringArray.test(exclude_impl=["implname"])
            async def test_logic(TestFnNamedArgsSingleStringArrayImpl: ITestFnNamedArgsSingleStringArray) -> None:
                result = await TestFnNamedArgsSingleStringArrayImpl(...)
            ```

            ```python
            # Streamable version of the test function.

            @baml.TestFnNamedArgsSingleStringArray.test(stream=True)
            async def test_logic(TestFnNamedArgsSingleStringArrayImpl: ITestFnNamedArgsSingleStringArrayStream) -> None:
                async for result in TestFnNamedArgsSingleStringArrayImpl(...):
                    ...
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the TestFnNamedArgsSingleStringArrayInterface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.TestFnNamedArgsSingleStringArray.test
        class TestClass:
            def test_a(self, TestFnNamedArgsSingleStringArrayImpl: ITestFnNamedArgsSingleStringArray) -> None:
                ...
            def test_b(self, TestFnNamedArgsSingleStringArrayImpl: ITestFnNamedArgsSingleStringArray) -> None:
                ...
        ```
        """
        ...

BAMLTestFnNamedArgsSingleStringArray: IBAMLTestFnNamedArgsSingleStringArray