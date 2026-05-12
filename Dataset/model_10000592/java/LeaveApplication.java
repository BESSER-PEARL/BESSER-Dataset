




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private LocalDate fromDate;
    private String approverComments;
    private String employeeId;
    private String applicationId;
    private String status;
    private LocalDate toDate;
    private String reason;



    public LeaveApplication(
        LocalDate fromDate,        String approverComments,        String employeeId,        String applicationId,        String status,        LocalDate toDate,        String reason    ) {
        this.fromDate = fromDate;
        this.approverComments = approverComments;
        this.employeeId = employeeId;
        this.applicationId = applicationId;
        this.status = status;
        this.toDate = toDate;
        this.reason = reason;
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


}