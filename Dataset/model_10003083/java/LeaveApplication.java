




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private String approverComments;
    private String status;
    private LocalDate fromDate;
    private String studentId;
    private String reason;
    private String applicationId;
    private LocalDate toDate;



    public LeaveApplication(
        String approverComments,        String status,        LocalDate fromDate,        String studentId,        String reason,        String applicationId,        LocalDate toDate    ) {
        this.approverComments = approverComments;
        this.status = status;
        this.fromDate = fromDate;
        this.studentId = studentId;
        this.reason = reason;
        this.applicationId = applicationId;
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
    public LocalDate getFromdate() {
        return fromDate;
    }

    public void setFromdate(LocalDate fromDate) {
        this.fromDate = fromDate;
    }
    public String getStudentid() {
        return studentId;
    }

    public void setStudentid(String studentId) {
        this.studentId = studentId;
    }
    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
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