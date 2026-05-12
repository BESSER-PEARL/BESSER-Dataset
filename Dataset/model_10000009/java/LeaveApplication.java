




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private String applicationId;
    private String approverComments;
    private LocalDate toDate;
    private String employeeId;
    private String status;
    private LocalDate fromDate;
    private String reason;



    public LeaveApplication(
        String applicationId,        String approverComments,        LocalDate toDate,        String employeeId,        String status,        LocalDate fromDate,        String reason    ) {
        this.applicationId = applicationId;
        this.approverComments = approverComments;
        this.toDate = toDate;
        this.employeeId = employeeId;
        this.status = status;
        this.fromDate = fromDate;
        this.reason = reason;
    }


    public String getApplicationid() {
        return applicationId;
    }

    public void setApplicationid(String applicationId) {
        this.applicationId = applicationId;
    }
    public String getApprovercomments() {
        return approverComments;
    }

    public void setApprovercomments(String approverComments) {
        this.approverComments = approverComments;
    }
    public LocalDate getTodate() {
        return toDate;
    }

    public void setTodate(LocalDate toDate) {
        this.toDate = toDate;
    }
    public String getEmployeeid() {
        return employeeId;
    }

    public void setEmployeeid(String employeeId) {
        this.employeeId = employeeId;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public LocalDate getFromdate() {
        return fromDate;
    }

    public void setFromdate(LocalDate fromDate) {
        this.fromDate = fromDate;
    }
    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }


}