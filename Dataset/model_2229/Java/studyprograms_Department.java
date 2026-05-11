





import java.util.List;
import java.util.ArrayList;

public class studyprograms_Department  {

    private String name;
    private String code;





    private List<studyprograms_Course> studyprograms_courses;




    private List<studyprograms_Programme> studyprograms_programmes;


    public studyprograms_Department(
        String name,        String code    ) {
        this.name = name;
        this.code = code;
        this.studyprograms_courses = new ArrayList<>();
        this.studyprograms_programmes = new ArrayList<>();
    }

    public studyprograms_Department(
        String name,        String code        ArrayList<studyprograms_Course> studyprograms_courses,        ArrayList<studyprograms_Programme> studyprograms_programmes    ) {
        this.name = name;
        this.code = code;
        this.studyprograms_courses = studyprograms_courses;
        this.studyprograms_programmes = studyprograms_programmes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public List<studyprograms_Course> getStudyprograms_courses() {
        return studyprograms_courses;
    }

    public void addStudyprograms_course(Studyprograms_course studyprograms_course) {
        this.studyprograms_courses.add(studyprograms_course);
    }
    public List<studyprograms_Programme> getStudyprograms_programmes() {
        return studyprograms_programmes;
    }

    public void addStudyprograms_programme(Studyprograms_programme studyprograms_programme) {
        this.studyprograms_programmes.add(studyprograms_programme);
    }

}