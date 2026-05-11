





import java.util.List;
import java.util.ArrayList;

public class tDT4250_asssignment1_2_Semester  {

    private String Credits;
    private int Number;





    private tDT4250_asssignment1_2_Specialization tdt4250_asssignment1_2_specialization;




    private tDT4250_asssignment1_2_Program tdt4250_asssignment1_2_program;




    private List<tDT4250_asssignment1_2_Semester_Course> tdt4250_asssignment1_2_semester_courses;


    public tDT4250_asssignment1_2_Semester(
        String Credits,        int Number    ) {
        this.Credits = Credits;
        this.Number = Number;
        this.tdt4250_asssignment1_2_semester_courses = new ArrayList<>();
    }

    public tDT4250_asssignment1_2_Semester(
        String Credits,        int Number        ArrayList<tDT4250_asssignment1_2_Semester_Course> tdt4250_asssignment1_2_semester_courses    ) {
        this.Credits = Credits;
        this.Number = Number;
        this.tdt4250_asssignment1_2_semester_courses = tdt4250_asssignment1_2_semester_courses;
    }

    public String getCredits() {
        return Credits;
    }

    public void setCredits(String Credits) {
        this.Credits = Credits;
    }
    public int getNumber() {
        return Number;
    }

    public void setNumber(int Number) {
        this.Number = Number;
    }

    public tDT4250_asssignment1_2_Specialization getTdt4250_asssignment1_2_specialization() {
        return tdt4250_asssignment1_2_specialization;
    }

    public void setTdt4250_asssignment1_2_specialization(tDT4250_asssignment1_2_Specialization tdt4250_asssignment1_2_specialization) {
        this.tdt4250_asssignment1_2_specialization = tdt4250_asssignment1_2_specialization;
    }
    public tDT4250_asssignment1_2_Program getTdt4250_asssignment1_2_program() {
        return tdt4250_asssignment1_2_program;
    }

    public void setTdt4250_asssignment1_2_program(tDT4250_asssignment1_2_Program tdt4250_asssignment1_2_program) {
        this.tdt4250_asssignment1_2_program = tdt4250_asssignment1_2_program;
    }
    public List<tDT4250_asssignment1_2_Semester_Course> getTdt4250_asssignment1_2_semester_courses() {
        return tdt4250_asssignment1_2_semester_courses;
    }

    public void addTdt4250_asssignment1_2_semester_course(Tdt4250_asssignment1_2_semester_course tdt4250_asssignment1_2_semester_course) {
        this.tdt4250_asssignment1_2_semester_courses.add(tdt4250_asssignment1_2_semester_course);
    }

}