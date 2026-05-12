




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private String applicationId;
    private LocalDate toDate;
    private String status;
    private String approverComments;
    private LocalDate fromDate;
    private String employeeId;
    private String reason;



    public LeaveApplication(
        String applicationId,        LocalDate toDate,        String status,        String approverComments,        LocalDate fromDate,        String employeeId,        String reason    ) {
        this.applicationId = applicationId;
        this.toDate = toDate;
        this.status = status;
        this.approverComments = approverComments;
        this.fromDate = fromDate;
        this.employeeId = employeeId;
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
    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }


}