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
    from ......models.o_data_errors.o_data_error import ODataError
    from ......models.print_job import PrintJob
    from .abort.abort_request_builder import AbortRequestBuilder
    from .cancel.cancel_request_builder import CancelRequestBuilder
    from .documents.documents_request_builder import DocumentsRequestBuilder
    from .redirect.redirect_request_builder import RedirectRequestBuilder
    from .start.start_request_builder import StartRequestBuilder
    from .tasks.tasks_request_builder import TasksRequestBuilder

class PrintJobItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the jobs property of the microsoft.graph.printerBase entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PrintJobItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/print/printers/{printer%2Did}/jobs/{printJob%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Delete navigation property jobs for print
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[PrintJob]:
        """
        The list of jobs that are queued for printing by the printer/printerShare.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PrintJob]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.print_job import PrintJob

        return await self.request_adapter.send_async(request_info, PrintJob, error_mapping)
    
    async def patch(self,body: Optional[PrintJob] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[PrintJob]:
        """
        Update the navigation property jobs in print
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PrintJob]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.print_job import PrintJob

        return await self.request_adapter.send_async(request_info, PrintJob, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property jobs for print
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/print/printers/{printer%2Did}/jobs/{printJob%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        The list of jobs that are queued for printing by the printer/printerShare.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[PrintJob] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property jobs in print
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, '{+baseurl}/print/printers/{printer%2Did}/jobs/{printJob%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> PrintJobItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PrintJobItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return PrintJobItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def abort(self) -> AbortRequestBuilder:
        """
        Provides operations to call the abort method.
        """
        from .abort.abort_request_builder import AbortRequestBuilder

        return AbortRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cancel(self) -> CancelRequestBuilder:
        """
        Provides operations to call the cancel method.
        """
        from .cancel.cancel_request_builder import CancelRequestBuilder

        return CancelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def documents(self) -> DocumentsRequestBuilder:
        """
        Provides operations to manage the documents property of the microsoft.graph.printJob entity.
        """
        from .documents.documents_request_builder import DocumentsRequestBuilder

        return DocumentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def redirect(self) -> RedirectRequestBuilder:
        """
        Provides operations to call the redirect method.
        """
        from .redirect.redirect_request_builder import RedirectRequestBuilder

        return RedirectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def start(self) -> StartRequestBuilder:
        """
        Provides operations to call the start method.
        """
        from .start.start_request_builder import StartRequestBuilder

        return StartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tasks(self) -> TasksRequestBuilder:
        """
        Provides operations to manage the tasks property of the microsoft.graph.printJob entity.
        """
        from .tasks.tasks_request_builder import TasksRequestBuilder

        return TasksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PrintJobItemRequestBuilderGetQueryParameters():
        """
        The list of jobs that are queued for printing by the printer/printerShare.
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

    

