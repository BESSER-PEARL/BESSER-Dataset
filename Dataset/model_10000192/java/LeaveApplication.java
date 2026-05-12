




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private LocalDate toDate;
    private String reason;
    private String employeeId;
    private String applicationId;
    private String approverComments;
    private String status;
    private LocalDate fromDate;



    public LeaveApplication(
        LocalDate toDate,        String reason,        String employeeId,        String applicationId,        String approverComments,        String status,        LocalDate fromDate    ) {
        this.toDate = toDate;
        this.reason = reason;
        this.employeeId = employeeId;
        this.applicationId = applicationId;
        this.approverComments = approverComments;
        this.status = status;
        this.fromDate = fromDate;
    }


    public LocalDate getTodate() {
        return toDate;
    }

    public void setTodate(LocalDate toDate) {
        this.toDate = toDate;
    }
    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }
    public String getEmployeeid() {
        return employeeId;
    }

    public void setEmployeeid(String employeeId) {
        this.employeeId = employeeId;
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


}