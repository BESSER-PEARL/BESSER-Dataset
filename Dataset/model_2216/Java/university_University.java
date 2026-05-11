





import java.util.List;
import java.util.ArrayList;

public class university_University  {

    private String name;





    private List<university_Programmes> university_programmess;




    private List<university_Courses> university_coursess;


    public university_University(
        String name    ) {
        this.name = name;
        this.university_programmess = new ArrayList<>();
        this.university_coursess = new ArrayList<>();
    }

    public university_University(
        String name        ArrayList<university_Programmes> university_programmess,        ArrayList<university_Courses> university_coursess    ) {
        this.name = name;
        this.university_programmess = university_programmess;
        this.university_coursess = university_coursess;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<university_Programmes> getUniversity_programmess() {
        return university_programmess;
    }

    public void addUniversity_programmes(University_programmes university_programmes) {
        this.university_programmess.add(university_programmes);
    }
    public List<university_Courses> getUniversity_coursess() {
        return university_coursess;
    }

    public void addUniversity_courses(University_courses university_courses) {
        this.university_coursess.add(university_courses);
    }

}