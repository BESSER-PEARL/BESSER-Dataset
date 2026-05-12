




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private LocalDate toDate;
    private String reason;
    private String status;
    private String applicationId;
    private LocalDate fromDate;
    private String approverComments;
    private String employeeId;



    public LeaveApplication(
        LocalDate toDate,        String reason,        String status,        String applicationId,        LocalDate fromDate,        String approverComments,        String employeeId    ) {
        this.toDate = toDate;
        this.reason = reason;
        this.status = status;
        this.applicationId = applicationId;
        this.fromDate = fromDate;
        this.approverComments = approverComments;
        this.employeeId = employeeId;
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


}