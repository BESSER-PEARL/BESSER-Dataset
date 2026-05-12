




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private String reason;
    private String employeeId;
    private LocalDate fromDate;
    private String status;
    private LocalDate toDate;
    private String approverComments;
    private String applicationId;



    public LeaveApplication(
        String reason,        String employeeId,        LocalDate fromDate,        String status,        LocalDate toDate,        String approverComments,        String applicationId    ) {
        this.reason = reason;
        this.employeeId = employeeId;
        this.fromDate = fromDate;
        this.status = status;
        this.toDate = toDate;
        this.approverComments = approverComments;
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


}