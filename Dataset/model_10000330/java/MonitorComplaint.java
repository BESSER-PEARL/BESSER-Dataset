




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class MonitorComplaint  {

    private int complaintid;
    private LocalDate date;
    private String complainttype;



    public MonitorComplaint(
        int complaintid,        LocalDate date,        String complainttype    ) {
        this.complaintid = complaintid;
        this.date = date;
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
    public String getComplainttype() {
        return complainttype;
    }

    public void setComplainttype(String complainttype) {
        this.complainttype = complainttype;
    }


}