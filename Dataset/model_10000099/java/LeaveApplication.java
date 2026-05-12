




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private String applicationId;
    private LocalDate toDate;
    private String employeeId;
    private LocalDate fromDate;
    private String approverComments;
    private String status;
    private String reason;



    public LeaveApplication(
        String applicationId,        LocalDate toDate,        String employeeId,        LocalDate fromDate,        String approverComments,        String status,        String reason    ) {
        this.applicationId = applicationId;
        this.toDate = toDate;
        this.employeeId = employeeId;
        this.fromDate = fromDate;
        this.approverComments = approverComments;
        this.status = status;
        this.reason = reason;
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
    public String getEmployeeid() {
        return employeeId;
    }

    public void setEmployeeid(String employeeId) {
        this.employeeId = employeeId;
    }
    public LocalDate getFromdate() {
        return fromDate;
    }

    public void setFromdate(LocalDate fromDate) {
        this.fromDate = fromDate;
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
    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }


}