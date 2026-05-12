





import java.util.List;
import java.util.ArrayList;

public class mypackage_Tutor  {

    private String TutorFileName;
    private String WorkingHours;



    public mypackage_Tutor(
        String TutorFileName,        String WorkingHours    ) {
        this.TutorFileName = TutorFileName;
        this.WorkingHours = WorkingHours;
    }


    public String getTutorfilename() {
        return TutorFileName;
    }

    public void setTutorfilename(String TutorFileName) {
        this.TutorFileName = TutorFileName;
    }
    public String getWorkinghours() {
        return WorkingHours;
    }

    public void setWorkinghours(String WorkingHours) {
        this.WorkingHours = WorkingHours;
    }


}