




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private String reason;
    private LocalDate toDate;
    private String status;
    private String employeeId;
    private String approverComments;
    private LocalDate fromDate;
    private String applicationId;



    public LeaveApplication(
        String reason,        LocalDate toDate,        String status,        String employeeId,        String approverComments,        LocalDate fromDate,        String applicationId    ) {
        this.reason = reason;
        this.toDate = toDate;
        this.status = status;
        this.employeeId = employeeId;
        this.approverComments = approverComments;
        this.fromDate = fromDate;
        this.applicationId = applicationId;
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
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getEmployeeid() {
        return employeeId;
    }

    public void setEmployeeid(String employeeId) {
        this.employeeId = employeeId;
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
    public String getApplicationid() {
        return applicationId;
    }

    public void setApplicationid(String applicationId) {
        this.applicationId = applicationId;
    }


}