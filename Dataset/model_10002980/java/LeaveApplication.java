




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private String applicationId;
    private String employeeId;
    private LocalDate toDate;
    private String status;
    private String reason;
    private String approverComments;
    private LocalDate fromDate;



    public LeaveApplication(
        String applicationId,        String employeeId,        LocalDate toDate,        String status,        String reason,        String approverComments,        LocalDate fromDate    ) {
        this.applicationId = applicationId;
        this.employeeId = employeeId;
        this.toDate = toDate;
        this.status = status;
        this.reason = reason;
        this.approverComments = approverComments;
        this.fromDate = fromDate;
    }


    public String getApplicationid() {
        return applicationId;
    }

    public void setApplicationid(String applicationId) {
        this.applicationId = applicationId;
    }
    public String getEmployeeid() {
        return employeeId;
    }

    public void setEmployeeid(String employeeId) {
        this.employeeId = employeeId;
    }
    public LocalDate getTodate() {
        return toDate;
    }

    public void setTodate(LocalDate toDate) {
        this.toDate = toDate;
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
    public String getApprovercomments() {
        return approverComments;
    }

    public void setApprovercomments(String approverComments) {
        this.approverComments = approverComments;
    }
    public LocalDate getFromdate() {
        return fromDate;
    }

    public void setFromdate(LocalDate fromDate) {
        this.fromDate = fromDate;
    }


}