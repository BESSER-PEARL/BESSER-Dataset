





import java.util.List;
import java.util.ArrayList;

public class tDT4250_asssignment1_2_Program_course  {

    private boolean Mandatory;
    private String Fall_or_spring;





    private List<tDT4250_asssignment1_2_Course> tdt4250_asssignment1_2_courses;




    private tDT4250_asssignment1_2_Program tdt4250_asssignment1_2_program;


    public tDT4250_asssignment1_2_Program_course(
        boolean Mandatory,        String Fall_or_spring    ) {
        this.Mandatory = Mandatory;
        this.Fall_or_spring = Fall_or_spring;
        this.tdt4250_asssignment1_2_courses = new ArrayList<>();
    }

    public tDT4250_asssignment1_2_Program_course(
        boolean Mandatory,        String Fall_or_spring        ArrayList<tDT4250_asssignment1_2_Course> tdt4250_asssignment1_2_courses    ) {
        this.Mandatory = Mandatory;
        this.Fall_or_spring = Fall_or_spring;
        this.tdt4250_asssignment1_2_courses = tdt4250_asssignment1_2_courses;
    }

    public boolean getMandatory() {
        return Mandatory;
    }

    public void setMandatory(boolean Mandatory) {
        this.Mandatory = Mandatory;
    }
    public String getFall_or_spring() {
        return Fall_or_spring;
    }

    public void setFall_or_spring(String Fall_or_spring) {
        this.Fall_or_spring = Fall_or_spring;
    }

    public List<tDT4250_asssignment1_2_Course> getTdt4250_asssignment1_2_courses() {
        return tdt4250_asssignment1_2_courses;
    }

    public void addTdt4250_asssignment1_2_course(Tdt4250_asssignment1_2_course tdt4250_asssignment1_2_course) {
        this.tdt4250_asssignment1_2_courses.add(tdt4250_asssignment1_2_course);
    }
    public tDT4250_asssignment1_2_Program getTdt4250_asssignment1_2_program() {
        return tdt4250_asssignment1_2_program;
    }

    public void setTdt4250_asssignment1_2_program(tDT4250_asssignment1_2_Program tdt4250_asssignment1_2_program) {
        this.tdt4250_asssignment1_2_program = tdt4250_asssignment1_2_program;
    }

}