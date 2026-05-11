





import java.util.List;
import java.util.ArrayList;

public class course_desc_Department  {

    private String name;





    private course_desc_Univ course_desc_univ;




    private course_desc_CourseInstance course_desc_courseinstance;




    private List<course_desc_StudyProgram> course_desc_studyprograms;




    private course_desc_StudyProgram course_desc_studyprogram;




    private List<course_desc_CourseInstance> course_desc_courseinstances;


    public course_desc_Department(
        String name    ) {
        this.name = name;
        this.course_desc_studyprograms = new ArrayList<>();
        this.course_desc_courseinstances = new ArrayList<>();
    }

    public course_desc_Department(
        String name        ArrayList<course_desc_StudyProgram> course_desc_studyprograms,        ArrayList<course_desc_CourseInstance> course_desc_courseinstances    ) {
        this.name = name;
        this.course_desc_studyprograms = course_desc_studyprograms;
        this.course_desc_courseinstances = course_desc_courseinstances;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public course_desc_Univ getCourse_desc_univ() {
        return course_desc_univ;
    }

    public void setCourse_desc_univ(course_desc_Univ course_desc_univ) {
        this.course_desc_univ = course_desc_univ;
    }
    public course_desc_CourseInstance getCourse_desc_courseinstance() {
        return course_desc_courseinstance;
    }

    public void setCourse_desc_courseinstance(course_desc_CourseInstance course_desc_courseinstance) {
        this.course_desc_courseinstance = course_desc_courseinstance;
    }
    public List<course_desc_StudyProgram> getCourse_desc_studyprograms() {
        return course_desc_studyprograms;
    }

    public void addCourse_desc_studyprogram(Course_desc_studyprogram course_desc_studyprogram) {
        this.course_desc_studyprograms.add(course_desc_studyprogram);
    }
    public course_desc_StudyProgram getCourse_desc_studyprogram() {
        return course_desc_studyprogram;
    }

    public void setCourse_desc_studyprogram(course_desc_StudyProgram course_desc_studyprogram) {
        this.course_desc_studyprogram = course_desc_studyprogram;
    }
    public List<course_desc_CourseInstance> getCourse_desc_courseinstances() {
        return course_desc_courseinstances;
    }

    public void addCourse_desc_courseinstance(Course_desc_courseinstance course_desc_courseinstance) {
        this.course_desc_courseinstances.add(course_desc_courseinstance);
    }

}