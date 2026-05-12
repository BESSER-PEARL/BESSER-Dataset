




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private LocalDate fromDate;
    private String employeeId;
    private LocalDate toDate;
    private String approverComments;
    private String applicationId;
    private String reason;
    private String status;



    public LeaveApplication(
        LocalDate fromDate,        String employeeId,        LocalDate toDate,        String approverComments,        String applicationId,        String reason,        String status    ) {
        this.fromDate = fromDate;
        this.employeeId = employeeId;
        this.toDate = toDate;
        this.approverComments = approverComments;
        this.applicationId = applicationId;
        this.reason = reason;
        this.status = status;
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
    public LocalDate getTodate() {
        return toDate;
    }

    public void setTodate(LocalDate toDate) {
        this.toDate = toDate;
    }
    public String getApprovercomments() {
        return approverComments;
    }

    public void setApprovercomments(String approverComments) {
        this.approverComments = approverComments;
    }
    public String getApplicationid() {
        return applicationId;
    }

    public void setApplicationid(String applicationId) {
        this.applicationId = applicationId;
    }
    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


}