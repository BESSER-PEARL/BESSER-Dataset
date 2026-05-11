





import java.util.List;
import java.util.ArrayList;

public class course_desc_Timetable  {






    private List<course_desc_CourseWork> course_desc_courseworks;




    private course_desc_CourseInstance course_desc_courseinstance;




    private List<course_desc_StudyProgram> course_desc_studyprograms;


    public course_desc_Timetable(
    ) {
        this.course_desc_courseworks = new ArrayList<>();
        this.course_desc_studyprograms = new ArrayList<>();
    }

    public course_desc_Timetable(
        ArrayList<course_desc_CourseWork> course_desc_courseworks,        ArrayList<course_desc_StudyProgram> course_desc_studyprograms    ) {
        this.course_desc_courseworks = course_desc_courseworks;
        this.course_desc_studyprograms = course_desc_studyprograms;
    }


    public List<course_desc_CourseWork> getCourse_desc_courseworks() {
        return course_desc_courseworks;
    }

    public void addCourse_desc_coursework(Course_desc_coursework course_desc_coursework) {
        this.course_desc_courseworks.add(course_desc_coursework);
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

}