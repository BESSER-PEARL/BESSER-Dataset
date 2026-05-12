





import java.util.List;
import java.util.ArrayList;

public class RegisterComplaint  {

    private String description;
    private String complainttype;



    public RegisterComplaint(
        String description,        String complainttype    ) {
        this.description = description;
        this.complainttype = complainttype;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getComplainttype() {
        return complainttype;
    }

    public void setComplainttype(String complainttype) {
        this.complainttype = complainttype;
    }


}