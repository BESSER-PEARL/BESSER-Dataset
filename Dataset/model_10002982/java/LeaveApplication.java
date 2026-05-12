




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private String reason;
    private String status;
    private String approverComments;
    private String studentId;
    private LocalDate fromDate;
    private String applicationId;
    private LocalDate toDate;



    public LeaveApplication(
        String reason,        String status,        String approverComments,        String studentId,        LocalDate fromDate,        String applicationId,        LocalDate toDate    ) {
        this.reason = reason;
        this.status = status;
        this.approverComments = approverComments;
        this.studentId = studentId;
        this.fromDate = fromDate;
        this.applicationId = applicationId;
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
    public String getApprovercomments() {
        return approverComments;
    }

    public void setApprovercomments(String approverComments) {
        this.approverComments = approverComments;
    }
    public String getStudentid() {
        return studentId;
    }

    public void setStudentid(String studentId) {
        this.studentId = studentId;
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
    public LocalDate getTodate() {
        return toDate;
    }

    public void setTodate(LocalDate toDate) {
        this.toDate = toDate;
    }


}