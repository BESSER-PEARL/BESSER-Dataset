





import java.util.List;
import java.util.ArrayList;

public class Univerity_Courses  {

    private String Name;
    private int CFU;
    private String Semester;





    private Univerity_Courses univerity_courses;


    public Univerity_Courses(
        String Name,        int CFU,        String Semester    ) {
        this.Name = Name;
        this.CFU = CFU;
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
    public String getSemester() {
        return Semester;
    }

    public void setSemester(String Semester) {
        this.Semester = Semester;
    }

    public Univerity_Courses getUniverity_courses() {
        return univerity_courses;
    }

    public void setUniverity_courses(Univerity_Courses univerity_courses) {
        this.univerity_courses = univerity_courses;
    }

}