




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private String reason;
    private LocalDate fromDate;
    private String status;
    private String approverComments;
    private String employeeId;
    private String applicationId;
    private LocalDate toDate;



    public LeaveApplication(
        String reason,        LocalDate fromDate,        String status,        String approverComments,        String employeeId,        String applicationId,        LocalDate toDate    ) {
        this.reason = reason;
        this.fromDate = fromDate;
        this.status = status;
        this.approverComments = approverComments;
        this.employeeId = employeeId;
        this.applicationId = applicationId;
        this.toDate = toDate;
    }


    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }
    public LocalDate getFromdate() {
        return fromDate;
    }

    public void setFromdate(LocalDate fromDate) {
        this.fromDate = fromDate;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getApprovercomments() {
        return approverComments;
    }

    public void setApprovercomments(String approverComments) {
        this.approverComments = approverComments;
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
    public LocalDate getTodate() {
        return toDate;
    }

    public void setTodate(LocalDate toDate) {
        this.toDate = toDate;
    }


}