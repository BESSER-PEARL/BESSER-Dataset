




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private LocalDate fromDate;
    private String status;
    private String approverComments;
    private LocalDate toDate;
    private String applicationId;
    private String reason;
    private String employeeId;



    public LeaveApplication(
        LocalDate fromDate,        String status,        String approverComments,        LocalDate toDate,        String applicationId,        String reason,        String employeeId    ) {
        this.fromDate = fromDate;
        this.status = status;
        this.approverComments = approverComments;
        this.toDate = toDate;
        this.applicationId = applicationId;
        this.reason = reason;
        this.employeeId = employeeId;
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
    public LocalDate getTodate() {
        return toDate;
    }

    public void setTodate(LocalDate toDate) {
        this.toDate = toDate;
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
    public String getEmployeeid() {
        return employeeId;
    }

    public void setEmployeeid(String employeeId) {
        this.employeeId = employeeId;
    }


}