




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private String employeeId;
    private LocalDate fromDate;
    private LocalDate toDate;
    private String status;
    private String approverComments;
    private String reason;
    private String applicationId;



    public LeaveApplication(
        String employeeId,        LocalDate fromDate,        LocalDate toDate,        String status,        String approverComments,        String reason,        String applicationId    ) {
        this.employeeId = employeeId;
        this.fromDate = fromDate;
        this.toDate = toDate;
        this.status = status;
        this.approverComments = approverComments;
        this.reason = reason;
        this.applicationId = applicationId;
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
    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }
    public String getApplicationid() {
        return applicationId;
    }

    public void setApplicationid(String applicationId) {
        this.applicationId = applicationId;
    }


}