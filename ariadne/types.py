from typing import (
    Any,
    AsyncGenerator,
    Callable,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)
from typing_extensions import Protocol

from graphql import DocumentNode, ExecutionResult, GraphQLError, GraphQLSchema
from graphql.validation.rules import ASTValidationRule


class SchemaBindable(Protocol):
    def bind_to_schema(self, schema: GraphQLSchema) -> None:
        pass  # pragma: no cover


# Note: this should be [Any, GraphQLResolveInfo, **kwargs],
# but this is not achieveable with python types yet:
# https://github.com/mirumee/ariadne/pull/79
Resolver = Callable[..., Any]
GraphQLResult = Tuple[bool, dict]
SubscriptionResult = Tuple[
    bool, Union[List[dict], AsyncGenerator[ExecutionResult, None]]
]
Subscriber = Callable[..., AsyncGenerator]
ErrorFormatter = Callable[[GraphQLError, bool], dict]

ContextValue = Union[Any, Callable[[Any], Any]]
RootValue = Union[Any, Callable[[Optional[Any], DocumentNode], Any]]
ValidationRules = Union[
    Sequence[Type[ASTValidationRule]],
    Callable[
        [Optional[Any], DocumentNode, dict], Optional[Sequence[Type[ASTValidationRule]]]
    ],
]
