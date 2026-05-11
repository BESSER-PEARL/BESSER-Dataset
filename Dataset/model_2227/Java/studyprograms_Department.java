





import java.util.List;
import java.util.ArrayList;

public class studyprograms_Department  {

    private String code;
    private String name;





    private List<studyprograms_Programme> studyprograms_programmes;




    private List<studyprograms_Course> studyprograms_courses;


    public studyprograms_Department(
        String code,        String name    ) {
        this.code = code;
        this.name = name;
        this.studyprograms_programmes = new ArrayList<>();
        this.studyprograms_courses = new ArrayList<>();
    }

    public studyprograms_Department(
        String code,        String name        ArrayList<studyprograms_Programme> studyprograms_programmes,        ArrayList<studyprograms_Course> studyprograms_courses    ) {
        this.code = code;
        this.name = name;
        this.studyprograms_programmes = studyprograms_programmes;
        this.studyprograms_courses = studyprograms_courses;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<studyprograms_Programme> getStudyprograms_programmes() {
        return studyprograms_programmes;
    }

    public void addStudyprograms_programme(Studyprograms_programme studyprograms_programme) {
        this.studyprograms_programmes.add(studyprograms_programme);
    }
    public List<studyprograms_Course> getStudyprograms_courses() {
        return studyprograms_courses;
    }

    public void addStudyprograms_course(Studyprograms_course studyprograms_course) {
        this.studyprograms_courses.add(studyprograms_course);
    }

}