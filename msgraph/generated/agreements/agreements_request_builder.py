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
    from ..models.agreement import Agreement
    from ..models.agreement_collection_response import AgreementCollectionResponse
    from ..models.o_data_errors.o_data_error import ODataError
    from .item.agreement_item_request_builder import AgreementItemRequestBuilder

class AgreementsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new AgreementsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/agreements{?%24search,%24select}", path_parameters)
    
    def by_agreement_id(self,agreement_id: str) -> AgreementItemRequestBuilder:
        """
        Provides operations to manage the collection of agreement entities.
        param agreement_id: The unique identifier of agreement
        Returns: AgreementItemRequestBuilder
        """
        if not agreement_id:
            raise TypeError("agreement_id cannot be null.")
        from .item.agreement_item_request_builder import AgreementItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agreement%2Did"] = agreement_id
        return AgreementItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[AgreementCollectionResponse]:
        """
        Get entities from agreements
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AgreementCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.agreement_collection_response import AgreementCollectionResponse

        return await self.request_adapter.send_async(request_info, AgreementCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[Agreement] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[Agreement]:
        """
        Add new entity to agreements
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Agreement]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.agreement import Agreement

        return await self.request_adapter.send_async(request_info, Agreement, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Get entities from agreements
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Optional[Agreement] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Add new entity to agreements
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, '{+baseurl}/agreements', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> AgreementsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AgreementsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return AgreementsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class AgreementsRequestBuilderGetQueryParameters():
        """
        Get entities from agreements
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    

