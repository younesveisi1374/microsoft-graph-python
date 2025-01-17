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
    from ........models.education_submission import EducationSubmission
    from ........models.o_data_errors.o_data_error import ODataError
    from .outcomes.outcomes_request_builder import OutcomesRequestBuilder
    from .reassign.reassign_request_builder import ReassignRequestBuilder
    from .resources.resources_request_builder import ResourcesRequestBuilder
    from .return_.return_request_builder import ReturnRequestBuilder
    from .set_up_resources_folder.set_up_resources_folder_request_builder import SetUpResourcesFolderRequestBuilder
    from .submit.submit_request_builder import SubmitRequestBuilder
    from .submitted_resources.submitted_resources_request_builder import SubmittedResourcesRequestBuilder
    from .unsubmit.unsubmit_request_builder import UnsubmitRequestBuilder

class EducationSubmissionItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the submissions property of the microsoft.graph.educationAssignment entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new EducationSubmissionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/education/classes/{educationClass%2Did}/assignments/{educationAssignment%2Did}/submissions/{educationSubmission%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Delete navigation property submissions for education
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[EducationSubmission]:
        """
        Retrieve a particular submission. Only teachers, students, and applications with application permissions can perform this operation. A submission object represents a student's work for an assignment. Resources associated with the submission represent this work. Only the assignedTo student can see and modify the submission. A teacher or application with application permissions has full access to all submissions. The grade and feedback from a teacher are part of the educationOutcome associated with this object. Only teachers or applications with application permissions can add or change grades and feedback. Students will not see the grade or feedback until the assignment has been released.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationSubmission]
        Find more info here: https://learn.microsoft.com/graph/api/educationsubmission-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.education_submission import EducationSubmission

        return await self.request_adapter.send_async(request_info, EducationSubmission, error_mapping)
    
    async def patch(self,body: Optional[EducationSubmission] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[EducationSubmission]:
        """
        Update the navigation property submissions in education
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationSubmission]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.education_submission import EducationSubmission

        return await self.request_adapter.send_async(request_info, EducationSubmission, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property submissions for education
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/education/classes/{educationClass%2Did}/assignments/{educationAssignment%2Did}/submissions/{educationSubmission%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve a particular submission. Only teachers, students, and applications with application permissions can perform this operation. A submission object represents a student's work for an assignment. Resources associated with the submission represent this work. Only the assignedTo student can see and modify the submission. A teacher or application with application permissions has full access to all submissions. The grade and feedback from a teacher are part of the educationOutcome associated with this object. Only teachers or applications with application permissions can add or change grades and feedback. Students will not see the grade or feedback until the assignment has been released.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[EducationSubmission] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property submissions in education
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, '{+baseurl}/education/classes/{educationClass%2Did}/assignments/{educationAssignment%2Did}/submissions/{educationSubmission%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> EducationSubmissionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EducationSubmissionItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return EducationSubmissionItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def outcomes(self) -> OutcomesRequestBuilder:
        """
        Provides operations to manage the outcomes property of the microsoft.graph.educationSubmission entity.
        """
        from .outcomes.outcomes_request_builder import OutcomesRequestBuilder

        return OutcomesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reassign(self) -> ReassignRequestBuilder:
        """
        Provides operations to call the reassign method.
        """
        from .reassign.reassign_request_builder import ReassignRequestBuilder

        return ReassignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resources(self) -> ResourcesRequestBuilder:
        """
        Provides operations to manage the resources property of the microsoft.graph.educationSubmission entity.
        """
        from .resources.resources_request_builder import ResourcesRequestBuilder

        return ResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def return_(self) -> ReturnRequestBuilder:
        """
        Provides operations to call the return method.
        """
        from .return_.return_request_builder import ReturnRequestBuilder

        return ReturnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_up_resources_folder(self) -> SetUpResourcesFolderRequestBuilder:
        """
        Provides operations to call the setUpResourcesFolder method.
        """
        from .set_up_resources_folder.set_up_resources_folder_request_builder import SetUpResourcesFolderRequestBuilder

        return SetUpResourcesFolderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def submit(self) -> SubmitRequestBuilder:
        """
        Provides operations to call the submit method.
        """
        from .submit.submit_request_builder import SubmitRequestBuilder

        return SubmitRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def submitted_resources(self) -> SubmittedResourcesRequestBuilder:
        """
        Provides operations to manage the submittedResources property of the microsoft.graph.educationSubmission entity.
        """
        from .submitted_resources.submitted_resources_request_builder import SubmittedResourcesRequestBuilder

        return SubmittedResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unsubmit(self) -> UnsubmitRequestBuilder:
        """
        Provides operations to call the unsubmit method.
        """
        from .unsubmit.unsubmit_request_builder import UnsubmitRequestBuilder

        return UnsubmitRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EducationSubmissionItemRequestBuilderGetQueryParameters():
        """
        Retrieve a particular submission. Only teachers, students, and applications with application permissions can perform this operation. A submission object represents a student's work for an assignment. Resources associated with the submission represent this work. Only the assignedTo student can see and modify the submission. A teacher or application with application permissions has full access to all submissions. The grade and feedback from a teacher are part of the educationOutcome associated with this object. Only teachers or applications with application permissions can add or change grades and feedback. Students will not see the grade or feedback until the assignment has been released.
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

    

