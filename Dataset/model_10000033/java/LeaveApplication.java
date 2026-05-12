




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private String status;
    private LocalDate toDate;
    private String employeeId;
    private String approverComments;
    private String reason;
    private LocalDate fromDate;
    private String applicationId;



    public LeaveApplication(
        String status,        LocalDate toDate,        String employeeId,        String approverComments,        String reason,        LocalDate fromDate,        String applicationId    ) {
        this.status = status;
        this.toDate = toDate;
        this.employeeId = employeeId;
        this.approverComments = approverComments;
        this.reason = reason;
        this.fromDate = fromDate;
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