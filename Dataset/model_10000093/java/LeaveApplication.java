




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private LocalDate toDate;
    private LocalDate fromDate;
    private String employeeId;
    private String applicationId;
    private String status;
    private String approverComments;
    private String reason;



    public LeaveApplication(
        LocalDate toDate,        LocalDate fromDate,        String employeeId,        String applicationId,        String status,        String approverComments,        String reason    ) {
        this.toDate = toDate;
        this.fromDate = fromDate;
        this.employeeId = employeeId;
        this.applicationId = applicationId;
        this.status = status;
        this.approverComments = approverComments;
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
    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }


}