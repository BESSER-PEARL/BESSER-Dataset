





import java.util.List;
import java.util.ArrayList;

public class tdt4250case_CourseInstance  {

    private String semester;





    private tdt4250case_Person tdt4250case_person;




    private tdt4250case_Timetable tdt4250case_timetable;




    private List<tdt4250case_CourseRole> tdt4250case_courseroles;




    private tdt4250case_Course tdt4250case_course;




    private tdt4250case_Examination tdt4250case_examination;




    private tdt4250case_Course tdt4250case_course;




    private tdt4250case_Department tdt4250case_department;


    public tdt4250case_CourseInstance(
        String semester    ) {
        this.semester = semester;
        this.tdt4250case_courseroles = new ArrayList<>();
    }

    public tdt4250case_CourseInstance(
        String semester        ArrayList<tdt4250case_CourseRole> tdt4250case_courseroles    ) {
        this.semester = semester;
        this.tdt4250case_courseroles = tdt4250case_courseroles;
    }

    public String getSemester() {
        return semester;
    }

    public void setSemester(String semester) {
        this.semester = semester;
    }

    public tdt4250case_Person getTdt4250case_person() {
        return tdt4250case_person;
    }

    public void setTdt4250case_person(tdt4250case_Person tdt4250case_person) {
        this.tdt4250case_person = tdt4250case_person;
    }
    public tdt4250case_Timetable getTdt4250case_timetable() {
        return tdt4250case_timetable;
    }

    public void setTdt4250case_timetable(tdt4250case_Timetable tdt4250case_timetable) {
        this.tdt4250case_timetable = tdt4250case_timetable;
    }
    public List<tdt4250case_CourseRole> getTdt4250case_courseroles() {
        return tdt4250case_courseroles;
    }

    public void addTdt4250case_courserole(Tdt4250case_courserole tdt4250case_courserole) {
        this.tdt4250case_courseroles.add(tdt4250case_courserole);
    }
    public tdt4250case_Course getTdt4250case_course() {
        return tdt4250case_course;
    }

    public void setTdt4250case_course(tdt4250case_Course tdt4250case_course) {
        this.tdt4250case_course = tdt4250case_course;
    }
    public tdt4250case_Examination getTdt4250case_examination() {
        return tdt4250case_examination;
    }

    public void setTdt4250case_examination(tdt4250case_Examination tdt4250case_examination) {
        this.tdt4250case_examination = tdt4250case_examination;
    }
    public tdt4250case_Course getTdt4250case_course() {
        return tdt4250case_course;
    }

    public void setTdt4250case_course(tdt4250case_Course tdt4250case_course) {
        this.tdt4250case_course = tdt4250case_course;
    }
    public tdt4250case_Department getTdt4250case_department() {
        return tdt4250case_department;
    }

    public void setTdt4250case_department(tdt4250case_Department tdt4250case_department) {
        this.tdt4250case_department = tdt4250case_department;
    }

}