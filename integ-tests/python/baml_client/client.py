###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
from typing import Dict, Generic, List, Optional, Tuple, TypeVar, Union
import pprint

import baml_py
from pydantic import BaseModel, ValidationError

from . import types

OutputType = TypeVar('OutputType')

class BamlOutputWrapper(BaseModel, Generic[OutputType]):
    wrapped: OutputType

class BamlClient:
    __runtime: baml_py.BamlRuntimeFfi

    @staticmethod
    def from_directory(path: str) -> "BamlClient":
      return BamlClient(runtime=baml_py.BamlRuntimeFfi.from_directory(path))

    def __init__(self, runtime: baml_py.BamlRuntimeFfi):
      self.__runtime = runtime

    async def ClassifyMessage(
        self,
        input: str
    ) -> types.Category:
      raw = await self.__runtime.call_function(
        "ClassifyMessage",
        {
          "input": input,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[types.Category].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for ClassifyMessage:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def ClassifyMessage2(
        self,
        input: str
    ) -> types.Category:
      raw = await self.__runtime.call_function(
        "ClassifyMessage2",
        {
          "input": input,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[types.Category].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for ClassifyMessage2:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def ClassifyMessage3(
        self,
        input: str
    ) -> types.Category:
      raw = await self.__runtime.call_function(
        "ClassifyMessage3",
        {
          "input": input,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[types.Category].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for ClassifyMessage3:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def ExtractNames(
        self,
        input: str
    ) -> List[str]:
      raw = await self.__runtime.call_function(
        "ExtractNames",
        {
          "input": input,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[List[str]].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for ExtractNames:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def ExtractResume(
        self,
        resume: str
    ) -> types.Resume:
      raw = await self.__runtime.call_function(
        "ExtractResume",
        {
          "resume": resume,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[types.Resume].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for ExtractResume:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def ExtractResume2(
        self,
        resume: str
    ) -> types.Resume:
      raw = await self.__runtime.call_function(
        "ExtractResume2",
        {
          "resume": resume,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[types.Resume].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for ExtractResume2:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def FnClassOptionalOutput2_V2(
        self,
        input: str
    ) -> Optional[types.ClassOptionalOutput2v2]:
      raw = await self.__runtime.call_function(
        "FnClassOptionalOutput2_V2",
        {
          "input": input,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[Optional[types.ClassOptionalOutput2v2]].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for FnClassOptionalOutput2_V2:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def FnOutputClassWithEnum_V2(
        self,
        input: str
    ) -> types.TestClassWithEnum2:
      raw = await self.__runtime.call_function(
        "FnOutputClassWithEnum_V2",
        {
          "input": input,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[types.TestClassWithEnum2].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for FnOutputClassWithEnum_V2:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def GetDataType(
        self,
        text: str
    ) -> types.RaysData:
      raw = await self.__runtime.call_function(
        "GetDataType",
        {
          "text": text,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[types.RaysData].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for GetDataType:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def GetOrderInfo(
        self,
        email: types.Email
    ) -> types.OrderInfo:
      raw = await self.__runtime.call_function(
        "GetOrderInfo",
        {
          "email": email,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[types.OrderInfo].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for GetOrderInfo:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def GetQuery(
        self,
        query: str
    ) -> types.SearchParams:
      raw = await self.__runtime.call_function(
        "GetQuery",
        {
          "query": query,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[types.SearchParams].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for GetQuery:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def OptionalTest_Function_V2(
        self,
        input: str
    ) -> List[Optional[types.OptionalTest_ReturnTypev2]]:
      raw = await self.__runtime.call_function(
        "OptionalTest_Function_V2",
        {
          "input": input,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[List[Optional[types.OptionalTest_ReturnTypev2]]].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for OptionalTest_Function_V2:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_FnClassOptional(
        self,
        input: Optional[types.OptionalClassv2]
    ) -> str:
      raw = await self.__runtime.call_function(
        "V2_FnClassOptional",
        {
          "input": input,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[str].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_FnClassOptional:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_FnClassOptional2(
        self,
        input: types.ClassOptionalFieldsv2
    ) -> str:
      raw = await self.__runtime.call_function(
        "V2_FnClassOptional2",
        {
          "input": input,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[str].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_FnClassOptional2:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_FnEnumListOutput(
        self,
        input: str
    ) -> List[types.EnumOutput]:
      raw = await self.__runtime.call_function(
        "V2_FnEnumListOutput",
        {
          "input": input,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[List[types.EnumOutput]].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_FnEnumListOutput:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_FnEnumOutput(
        self,
        input: str
    ) -> types.EnumOutput2:
      raw = await self.__runtime.call_function(
        "V2_FnEnumOutput",
        {
          "input": input,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[types.EnumOutput2].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_FnEnumOutput:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_FnNamedArgsSingleStringOptional(
        self,
        myString: Optional[str]
    ) -> str:
      raw = await self.__runtime.call_function(
        "V2_FnNamedArgsSingleStringOptional",
        {
          "myString": myString,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[str].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_FnNamedArgsSingleStringOptional:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_FnOutputBool(
        self,
        input: str
    ) -> bool:
      raw = await self.__runtime.call_function(
        "V2_FnOutputBool",
        {
          "input": input,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[bool].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_FnOutputBool:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_FnOutputClass(
        self,
        input: str
    ) -> types.TestOutputClass2:
      raw = await self.__runtime.call_function(
        "V2_FnOutputClass",
        {
          "input": input,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[types.TestOutputClass2].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_FnOutputClass:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_FnOutputClassList(
        self,
        input: str
    ) -> List[types.TestOutputClass]:
      raw = await self.__runtime.call_function(
        "V2_FnOutputClassList",
        {
          "input": input,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[List[types.TestOutputClass]].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_FnOutputClassList:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_FnOutputStringList(
        self,
        input: str
    ) -> List[str]:
      raw = await self.__runtime.call_function(
        "V2_FnOutputStringList",
        {
          "input": input,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[List[str]].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_FnOutputStringList:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_FnStringOptional(
        self,
        input: Optional[str]
    ) -> str:
      raw = await self.__runtime.call_function(
        "V2_FnStringOptional",
        {
          "input": input,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[str].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_FnStringOptional:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_FnTestNamedArgsSingleEnum(
        self,
        myArg: types.NamedArgsSingleEnum2
    ) -> str:
      raw = await self.__runtime.call_function(
        "V2_FnTestNamedArgsSingleEnum",
        {
          "myArg": myArg,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[str].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_FnTestNamedArgsSingleEnum:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_TestFnNamedArgsSingleBool(
        self,
        myBool: bool
    ) -> str:
      raw = await self.__runtime.call_function(
        "V2_TestFnNamedArgsSingleBool",
        {
          "myBool": myBool,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[str].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_TestFnNamedArgsSingleBool:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_TestFnNamedArgsSingleClass(
        self,
        myArg: types.NamedArgsSingleClass2
    ) -> str:
      raw = await self.__runtime.call_function(
        "V2_TestFnNamedArgsSingleClass",
        {
          "myArg": myArg,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[str].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_TestFnNamedArgsSingleClass:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_TestFnNamedArgsSingleEnumList(
        self,
        myArg: List[types.NamedArgsSingleEnumList2]
    ) -> str:
      raw = await self.__runtime.call_function(
        "V2_TestFnNamedArgsSingleEnumList",
        {
          "myArg": myArg,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[str].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_TestFnNamedArgsSingleEnumList:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_TestFnNamedArgsSingleFloat(
        self,
        myFloat: float
    ) -> str:
      raw = await self.__runtime.call_function(
        "V2_TestFnNamedArgsSingleFloat",
        {
          "myFloat": myFloat,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[str].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_TestFnNamedArgsSingleFloat:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_TestFnNamedArgsSingleInt(
        self,
        myInt: int
    ) -> str:
      raw = await self.__runtime.call_function(
        "V2_TestFnNamedArgsSingleInt",
        {
          "myInt": myInt,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[str].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_TestFnNamedArgsSingleInt:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_TestFnNamedArgsSingleString(
        self,
        myString: str
    ) -> str:
      raw = await self.__runtime.call_function(
        "V2_TestFnNamedArgsSingleString",
        {
          "myString": myString,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[str].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_TestFnNamedArgsSingleString:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_TestFnNamedArgsSingleStringArray(
        self,
        myStringArray: List[str]
    ) -> str:
      raw = await self.__runtime.call_function(
        "V2_TestFnNamedArgsSingleStringArray",
        {
          "myStringArray": myStringArray,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[str].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_TestFnNamedArgsSingleStringArray:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_TestFnNamedArgsSingleStringList(
        self,
        myArg: List[types.NamedArgsSingleClassList2]
    ) -> str:
      raw = await self.__runtime.call_function(
        "V2_TestFnNamedArgsSingleStringList",
        {
          "myArg": myArg,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[str].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_TestFnNamedArgsSingleStringList:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_TestFnNamedArgsSyntax(
        self,
        var: str,var_with_underscores: str
    ) -> str:
      raw = await self.__runtime.call_function(
        "V2_TestFnNamedArgsSyntax",
        {
          "var": var,"var_with_underscores": var_with_underscores,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[str].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_TestFnNamedArgsSyntax:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    async def V2_UnionTest_Function(
        self,
        input: Union[str, bool]
    ) -> Union[types.UnionTest_ReturnTypev2, types.DataType]:
      raw = await self.__runtime.call_function(
        "V2_UnionTest_Function",
        {
          "input": input,
        },
        ctx={}
      )
      parsed = raw.parsed()
      try:
        return BamlOutputWrapper[Union[types.UnionTest_ReturnTypev2, types.DataType]].model_validate(obj={'wrapped': parsed}).wrapped
      except ValidationError as e:
        raise TypeError(
          "Internal BAML error while mapping the FFI output type for V2_UnionTest_Function:\n{}".format(
            pprint.pformat(parsed)
          )
        ) from e

    