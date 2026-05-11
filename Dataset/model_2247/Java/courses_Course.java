





import java.util.List;
import java.util.ArrayList;

public class courses_Course  {

    private float credit;
    private String name;
    private String code;





    private courses_StudyProgram courses_studyprogram;




    private courses_University courses_university;




    private courses_CourseInstance courses_courseinstance;




    private List<courses_CourseInstance> courses_courseinstances;




    private List<courses_StudyProgram> courses_studyprograms;




    private courses_CourseInstance courses_courseinstance;


    public courses_Course(
        float credit,        String name,        String code    ) {
        this.credit = credit;
        this.name = name;
        this.code = code;
        this.courses_courseinstances = new ArrayList<>();
        this.courses_studyprograms = new ArrayList<>();
    }

    public courses_Course(
        float credit,        String name,        String code        ArrayList<courses_CourseInstance> courses_courseinstances,        ArrayList<courses_StudyProgram> courses_studyprograms    ) {
        this.credit = credit;
        this.name = name;
        this.code = code;
        this.courses_courseinstances = courses_courseinstances;
        this.courses_studyprograms = courses_studyprograms;
    }

    public float getCredit() {
        return credit;
    }

    public void setCredit(float credit) {
        this.credit = credit;
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

    public courses_StudyProgram getCourses_studyprogram() {
        return courses_studyprogram;
    }

    public void setCourses_studyprogram(courses_StudyProgram courses_studyprogram) {
        this.courses_studyprogram = courses_studyprogram;
    }
    public courses_University getCourses_university() {
        return courses_university;
    }

    public void setCourses_university(courses_University courses_university) {
        this.courses_university = courses_university;
    }
    public courses_CourseInstance getCourses_courseinstance() {
        return courses_courseinstance;
    }

    public void setCourses_courseinstance(courses_CourseInstance courses_courseinstance) {
        this.courses_courseinstance = courses_courseinstance;
    }
    public List<courses_CourseInstance> getCourses_courseinstances() {
        return courses_courseinstances;
    }

    public void addCourses_courseinstance(Courses_courseinstance courses_courseinstance) {
        this.courses_courseinstances.add(courses_courseinstance);
    }
    public List<courses_StudyProgram> getCourses_studyprograms() {
        return courses_studyprograms;
    }

    public void addCourses_studyprogram(Courses_studyprogram courses_studyprogram) {
        this.courses_studyprograms.add(courses_studyprogram);
    }
    public courses_CourseInstance getCourses_courseinstance() {
        return courses_courseinstance;
    }

    public void setCourses_courseinstance(courses_CourseInstance courses_courseinstance) {
        this.courses_courseinstance = courses_courseinstance;
    }

}