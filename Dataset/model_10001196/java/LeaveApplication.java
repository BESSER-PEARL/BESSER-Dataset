




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LeaveApplication  {

    private LocalDate fromDate;
    private String applicationId;
    private String reason;
    private String studentId;
    private LocalDate toDate;
    private String status;



    public LeaveApplication(
        LocalDate fromDate,        String applicationId,        String reason,        String studentId,        LocalDate toDate,        String status    ) {
        this.fromDate = fromDate;
        this.applicationId = applicationId;
        this.reason = reason;
        this.studentId = studentId;
        this.toDate = toDate;
        this.status = status;
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
    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
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
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


}