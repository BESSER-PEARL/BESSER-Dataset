





import java.util.List;
import java.util.ArrayList;

public class lMS_Course  {

    private String name;





    private lMS_LMS lms_lms;


    public lMS_Course(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public lMS_LMS getLms_lms() {
        return lms_lms;
    }

    public void setLms_lms(lMS_LMS lms_lms) {
        this.lms_lms = lms_lms;
    }

}