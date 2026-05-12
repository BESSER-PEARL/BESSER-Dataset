





import java.util.List;
import java.util.ArrayList;

public class monitor_complaint  {

    private int complaintid;
    private String complaint_type;
    private String date;



    public monitor_complaint(
        int complaintid,        String complaint_type,        String date    ) {
        this.complaintid = complaintid;
        this.complaint_type = complaint_type;
        this.date = date;
    }


    public int getComplaintid() {
        return complaintid;
    }

    public void setComplaintid(int complaintid) {
        this.complaintid = complaintid;
    }
    public String getComplaint_type() {
        return complaint_type;
    }

    public void setComplaint_type(String complaint_type) {
        this.complaint_type = complaint_type;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }


}