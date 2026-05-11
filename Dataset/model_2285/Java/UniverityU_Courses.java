





import java.util.List;
import java.util.ArrayList;

public class UniverityU_Courses extends uncertainty_aCourses, uncertainty_ModelElement {

    private String Semester;
    private String Name;
    private int CFU;



    public UniverityU_Courses(
        String Semester,        String Name,        int CFU    ) {
        super(
        );
        this.Semester = Semester;
        this.Name = Name;
        this.CFU = CFU;
    }


    public String getSemester() {
        return Semester;
    }

    public void setSemester(String Semester) {
        this.Semester = Semester;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getCfu() {
        return CFU;
    }

    public void setCfu(int CFU) {
        this.CFU = CFU;
    }


}