





import java.util.List;
import java.util.ArrayList;

public class monitor_complaint  {

    private String complaint_type;
    private int complaintid;
    private String date;



    public monitor_complaint(
        String complaint_type,        int complaintid,        String date    ) {
        this.complaint_type = complaint_type;
        this.complaintid = complaintid;
        this.date = date;
    }


    public String getComplaint_type() {
        return complaint_type;
    }

    public void setComplaint_type(String complaint_type) {
        this.complaint_type = complaint_type;
    }
    public int getComplaintid() {
        return complaintid;
    }

    public void setComplaintid(int complaintid) {
        this.complaintid = complaintid;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }


}