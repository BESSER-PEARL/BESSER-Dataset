




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private String employeeId;
    private String status;
    private String reason;
    private LocalDate toDate;
    private LocalDate fromDate;
    private String applicationId;
    private String approverComments;



    public LeaveApplication(
        String employeeId,        String status,        String reason,        LocalDate toDate,        LocalDate fromDate,        String applicationId,        String approverComments    ) {
        this.employeeId = employeeId;
        this.status = status;
        this.reason = reason;
        this.toDate = toDate;
        this.fromDate = fromDate;
        this.applicationId = applicationId;
        this.approverComments = approverComments;
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
    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }
    public LocalDate getTodate() {
        return toDate;
    }

    public void setTodate(LocalDate toDate) {
        this.toDate = toDate;
    }
    public LocalDate getFromdate() {
        return fromDate;
    }

    public void setFromdate(LocalDate fromDate) {
        this.fromDate = fromDate;
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


}