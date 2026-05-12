




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private LocalDate toDate;
    private LocalDate fromDate;
    private String reason;
    private String approverComments;
    private String studentId;
    private String applicationId;
    private String status;



    public LeaveApplication(
        LocalDate toDate,        LocalDate fromDate,        String reason,        String approverComments,        String studentId,        String applicationId,        String status    ) {
        this.toDate = toDate;
        this.fromDate = fromDate;
        this.reason = reason;
        this.approverComments = approverComments;
        this.studentId = studentId;
        this.applicationId = applicationId;
        this.status = status;
    }


    public LocalDate getTodate() {
        return toDate;
    }

    public void setTodate(LocalDate toDate) {
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
    public String getStudentid() {
        return studentId;
    }

    public void setStudentid(String studentId) {
        this.studentId = studentId;
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


}