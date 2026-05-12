




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class MonitorComplaint  {

    private String complainttype;
    private int complaintid;
    private LocalDate date;



    public MonitorComplaint(
        String complainttype,        int complaintid,        LocalDate date    ) {
        this.complainttype = complainttype;
        this.complaintid = complaintid;
        this.date = date;
    }


    public String getComplainttype() {
        return complainttype;
    }

    public void setComplainttype(String complainttype) {
        this.complainttype = complainttype;
    }
    public int getComplaintid() {
        return complaintid;
    }

    public void setComplaintid(int complaintid) {
        this.complaintid = complaintid;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }


}