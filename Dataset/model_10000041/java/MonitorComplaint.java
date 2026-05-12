




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class MonitorComplaint  {

    private String complainttype;
    private LocalDate date;
    private String complaintid;



    public MonitorComplaint(
        String complainttype,        LocalDate date,        String complaintid    ) {
        this.complainttype = complainttype;
        this.date = date;
        this.complaintid = complaintid;
    }


    public String getComplainttype() {
        return complainttype;
    }

    public void setComplainttype(String complainttype) {
        this.complainttype = complainttype;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getComplaintid() {
        return complaintid;
    }

    public void setComplaintid(String complaintid) {
        this.complaintid = complaintid;
    }


}