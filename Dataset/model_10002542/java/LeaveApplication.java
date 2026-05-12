




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private LocalDate fromDate;
    private String reason;
    private String approverComments;
    private String applicationId;
    private String status;
    private String studentId;
    private LocalDate toDate;



    public LeaveApplication(
        LocalDate fromDate,        String reason,        String approverComments,        String applicationId,        String status,        String studentId,        LocalDate toDate    ) {
        this.fromDate = fromDate;
        this.reason = reason;
        this.approverComments = approverComments;
        this.applicationId = applicationId;
        this.status = status;
        this.studentId = studentId;
        this.toDate = toDate;
    }


    public LocalDate getFromdate() {
        return fromDate;
    }

    public void setFromdate(LocalDate fromDate) {
        this.fromDate = fromDate;
    }
    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
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
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getStudentid() {
        return studentId;
    }

    public void setStudentid(String studentId) {
        this.studentId = studentId;
    }
    public LocalDate getTodate() {
        return toDate;
    }

    public void setTodate(LocalDate toDate) {
        this.toDate = toDate;
    }


}