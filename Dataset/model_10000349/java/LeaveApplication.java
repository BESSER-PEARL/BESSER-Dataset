




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private LocalDate toDate;
    private String approverComments;
    private String status;
    private String employeeId;
    private String reason;
    private LocalDate fromDate;
    private String applicationId;



    public LeaveApplication(
        LocalDate toDate,        String approverComments,        String status,        String employeeId,        String reason,        LocalDate fromDate,        String applicationId    ) {
        this.toDate = toDate;
        this.approverComments = approverComments;
        this.status = status;
        this.employeeId = employeeId;
        this.reason = reason;
        this.fromDate = fromDate;
        this.applicationId = applicationId;
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
    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
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