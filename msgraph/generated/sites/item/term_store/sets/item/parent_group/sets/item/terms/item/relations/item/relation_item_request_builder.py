from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .............models.o_data_errors.o_data_error import ODataError
    from .............models.term_store.relation import Relation
    from .from_term.from_term_request_builder import FromTermRequestBuilder
    from .set.set_request_builder import SetRequestBuilder
    from .to_term.to_term_request_builder import ToTermRequestBuilder

class RelationItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the relations property of the microsoft.graph.termStore.term entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new RelationItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/termStore/sets/{set%2Did}/parentGroup/sets/{set%2Did1}/terms/{term%2Did}/relations/{relation%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Delete navigation property relations for sites
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .............models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[Relation]:
        """
        To indicate which terms are related to the current term as either pinned or reused.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Relation]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .............models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .............models.term_store.relation import Relation

        return await self.request_adapter.send_async(request_info, Relation, error_mapping)
    
    async def patch(self,body: Optional[Relation] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[Relation]:
        """
        Update the navigation property relations in sites
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Relation]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .............models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .............models.term_store.relation import Relation

        return await self.request_adapter.send_async(request_info, Relation, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property relations for sites
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/sites/{site%2Did}/termStore/sets/{set%2Did}/parentGroup/sets/{set%2Did1}/terms/{term%2Did}/relations/{relation%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        To indicate which terms are related to the current term as either pinned or reused.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[Relation] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property relations in sites
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, '{+baseurl}/sites/{site%2Did}/termStore/sets/{set%2Did}/parentGroup/sets/{set%2Did1}/terms/{term%2Did}/relations/{relation%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> RelationItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RelationItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return RelationItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def from_term(self) -> FromTermRequestBuilder:
        """
        Provides operations to manage the fromTerm property of the microsoft.graph.termStore.relation entity.
        """
        from .from_term.from_term_request_builder import FromTermRequestBuilder

        return FromTermRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set(self) -> SetRequestBuilder:
        """
        Provides operations to manage the set property of the microsoft.graph.termStore.relation entity.
        """
        from .set.set_request_builder import SetRequestBuilder

        return SetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def to_term(self) -> ToTermRequestBuilder:
        """
        Provides operations to manage the toTerm property of the microsoft.graph.termStore.relation entity.
        """
        from .to_term.to_term_request_builder import ToTermRequestBuilder

        return ToTermRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class RelationItemRequestBuilderGetQueryParameters():
        """
        To indicate which terms are related to the current term as either pinned or reused.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    

