





import java.util.List;
import java.util.ArrayList;

public class tDT4250_asssignment1_2_Department  {

    private String Name;





    private List<tDT4250_asssignment1_2_Program> tdt4250_asssignment1_2_programs;




    private List<tDT4250_asssignment1_2_Course> tdt4250_asssignment1_2_courses;


    public tDT4250_asssignment1_2_Department(
        String Name    ) {
        this.Name = Name;
        this.tdt4250_asssignment1_2_programs = new ArrayList<>();
        this.tdt4250_asssignment1_2_courses = new ArrayList<>();
    }

    public tDT4250_asssignment1_2_Department(
        String Name        ArrayList<tDT4250_asssignment1_2_Program> tdt4250_asssignment1_2_programs,        ArrayList<tDT4250_asssignment1_2_Course> tdt4250_asssignment1_2_courses    ) {
        this.Name = Name;
        this.tdt4250_asssignment1_2_programs = tdt4250_asssignment1_2_programs;
        this.tdt4250_asssignment1_2_courses = tdt4250_asssignment1_2_courses;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<tDT4250_asssignment1_2_Program> getTdt4250_asssignment1_2_programs() {
        return tdt4250_asssignment1_2_programs;
    }

    public void addTdt4250_asssignment1_2_program(Tdt4250_asssignment1_2_program tdt4250_asssignment1_2_program) {
        this.tdt4250_asssignment1_2_programs.add(tdt4250_asssignment1_2_program);
    }
    public List<tDT4250_asssignment1_2_Course> getTdt4250_asssignment1_2_courses() {
        return tdt4250_asssignment1_2_courses;
    }

    public void addTdt4250_asssignment1_2_course(Tdt4250_asssignment1_2_course tdt4250_asssignment1_2_course) {
        this.tdt4250_asssignment1_2_courses.add(tdt4250_asssignment1_2_course);
    }

}