




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class MonitorComplaint  {

    private LocalDate date;
    private String complainttype;
    private String complaintid;



    public MonitorComplaint(
        LocalDate date,        String complainttype,        String complaintid    ) {
        this.date = date;
        this.complainttype = complainttype;
        this.complaintid = complaintid;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getComplainttype() {
        return complainttype;
    }

    public void setComplainttype(String complainttype) {
        this.complainttype = complainttype;
    }
    public String getComplaintid() {
        return complaintid;
    }

    public void setComplaintid(String complaintid) {
        this.complaintid = complaintid;
    }


}