





import java.util.List;
import java.util.ArrayList;

public class Employee_Actor  {






    private Approver_Jobs_UseCase approver_jobs_usecase;




    private Query_Leave_Balance_UseCase query_leave_balance_usecase;




    private Query_Leave_History_UseCase query_leave_history_usecase;




    private Apply_Leave_UseCase apply_leave_usecase;




    private Leave_Request_Status_UseCase leave_request_status_usecase;


    public Employee_Actor(
    ) {
    }



    public Approver_Jobs_UseCase getApprover_jobs_usecase() {
        return approver_jobs_usecase;
    }

    public void setApprover_jobs_usecase(Approver_Jobs_UseCase approver_jobs_usecase) {
        this.approver_jobs_usecase = approver_jobs_usecase;
    }
    public Query_Leave_Balance_UseCase getQuery_leave_balance_usecase() {
        return query_leave_balance_usecase;
    }

    public void setQuery_leave_balance_usecase(Query_Leave_Balance_UseCase query_leave_balance_usecase) {
        this.query_leave_balance_usecase = query_leave_balance_usecase;
    }
    public Query_Leave_History_UseCase getQuery_leave_history_usecase() {
        return query_leave_history_usecase;
    }

    public void setQuery_leave_history_usecase(Query_Leave_History_UseCase query_leave_history_usecase) {
        this.query_leave_history_usecase = query_leave_history_usecase;
    }
    public Apply_Leave_UseCase getApply_leave_usecase() {
        return apply_leave_usecase;
    }

    public void setApply_leave_usecase(Apply_Leave_UseCase apply_leave_usecase) {
        this.apply_leave_usecase = apply_leave_usecase;
    }
    public Leave_Request_Status_UseCase getLeave_request_status_usecase() {
        return leave_request_status_usecase;
    }

    public void setLeave_request_status_usecase(Leave_Request_Status_UseCase leave_request_status_usecase) {
        this.leave_request_status_usecase = leave_request_status_usecase;
    }

}