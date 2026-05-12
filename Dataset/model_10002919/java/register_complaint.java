





import java.util.List;
import java.util.ArrayList;

public class register_complaint  {

    private String description;
    private String complaint_type;



    public register_complaint(
        String description,        String complaint_type    ) {
        this.description = description;
        this.complaint_type = complaint_type;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getComplaint_type() {
        return complaint_type;
    }

    public void setComplaint_type(String complaint_type) {
        this.complaint_type = complaint_type;
    }


}