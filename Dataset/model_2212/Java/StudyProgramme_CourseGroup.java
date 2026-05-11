





import java.util.List;
import java.util.ArrayList;

public class StudyProgramme_CourseGroup  {

    private String status;





    private List<StudyProgramme_Course> studyprogramme_courses;




    private StudyProgramme_Semester studyprogramme_semester;


    public StudyProgramme_CourseGroup(
        String status    ) {
        this.status = status;
        this.studyprogramme_courses = new ArrayList<>();
    }

    public StudyProgramme_CourseGroup(
        String status        ArrayList<StudyProgramme_Course> studyprogramme_courses    ) {
        this.status = status;
        this.studyprogramme_courses = studyprogramme_courses;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public List<StudyProgramme_Course> getStudyprogramme_courses() {
        return studyprogramme_courses;
    }

    public void addStudyprogramme_course(Studyprogramme_course studyprogramme_course) {
        this.studyprogramme_courses.add(studyprogramme_course);
    }
    public StudyProgramme_Semester getStudyprogramme_semester() {
        return studyprogramme_semester;
    }

    public void setStudyprogramme_semester(StudyProgramme_Semester studyprogramme_semester) {
        this.studyprogramme_semester = studyprogramme_semester;
    }

}