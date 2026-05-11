





import java.util.List;
import java.util.ArrayList;

public class university_University  {

    private String name;





    private List<university_Professor> university_professors;




    private List<university_Course> university_courses;


    public university_University(
        String name    ) {
        this.name = name;
        this.university_professors = new ArrayList<>();
        this.university_courses = new ArrayList<>();
    }

    public university_University(
        String name        ArrayList<university_Professor> university_professors,        ArrayList<university_Course> university_courses    ) {
        this.name = name;
        this.university_professors = university_professors;
        this.university_courses = university_courses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<university_Professor> getUniversity_professors() {
        return university_professors;
    }

    public void addUniversity_professor(University_professor university_professor) {
        this.university_professors.add(university_professor);
    }
    public List<university_Course> getUniversity_courses() {
        return university_courses;
    }

    public void addUniversity_course(University_course university_course) {
        this.university_courses.add(university_course);
    }

}