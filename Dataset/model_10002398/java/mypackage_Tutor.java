





import java.util.List;
import java.util.ArrayList;

public class mypackage_Tutor  {

    private String TutorFileName;
    private String academicalHours;



    public mypackage_Tutor(
        String TutorFileName,        String academicalHours    ) {
        this.TutorFileName = TutorFileName;
        this.academicalHours = academicalHours;
    }


    public String getTutorfilename() {
        return TutorFileName;
    }

    public void setTutorfilename(String TutorFileName) {
        this.TutorFileName = TutorFileName;
    }
    public String getAcademicalhours() {
        return academicalHours;
    }

    public void setAcademicalhours(String academicalHours) {
        this.academicalHours = academicalHours;
    }


}