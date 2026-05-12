




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private String reason;
    private LocalDate fromDate;
    private String status;
    private String applicationId;
    private String approverComments;
    private LocalDate toDate;
    private String employeeId;



    public LeaveApplication(
        String reason,        LocalDate fromDate,        String status,        String applicationId,        String approverComments,        LocalDate toDate,        String employeeId    ) {
        this.reason = reason;
        this.fromDate = fromDate;
        this.status = status;
        this.applicationId = applicationId;
        this.approverComments = approverComments;
        this.toDate = toDate;
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
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getApplicationid() {
        return applicationId;
    }

    public void setApplicationid(String applicationId) {
        this.applicationId = applicationId;
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
    public String getEmployeeid() {
        return employeeId;
    }

    public void setEmployeeid(String employeeId) {
        this.employeeId = employeeId;
    }


}