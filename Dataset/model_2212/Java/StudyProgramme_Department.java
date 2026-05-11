





import java.util.List;
import java.util.ArrayList;

public class StudyProgramme_Department  {

    private String name;
    private String code;





    private List<StudyProgramme_Programme> studyprogramme_programmes;




    private List<StudyProgramme_Course> studyprogramme_courses;


    public StudyProgramme_Department(
        String name,        String code    ) {
        this.name = name;
        this.code = code;
        this.studyprogramme_programmes = new ArrayList<>();
        this.studyprogramme_courses = new ArrayList<>();
    }

    public StudyProgramme_Department(
        String name,        String code        ArrayList<StudyProgramme_Programme> studyprogramme_programmes,        ArrayList<StudyProgramme_Course> studyprogramme_courses    ) {
        this.name = name;
        this.code = code;
        this.studyprogramme_programmes = studyprogramme_programmes;
        this.studyprogramme_courses = studyprogramme_courses;
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

    public List<StudyProgramme_Programme> getStudyprogramme_programmes() {
        return studyprogramme_programmes;
    }

    public void addStudyprogramme_programme(Studyprogramme_programme studyprogramme_programme) {
        this.studyprogramme_programmes.add(studyprogramme_programme);
    }
    public List<StudyProgramme_Course> getStudyprogramme_courses() {
        return studyprogramme_courses;
    }

    public void addStudyprogramme_course(Studyprogramme_course studyprogramme_course) {
        this.studyprogramme_courses.add(studyprogramme_course);
    }

}