





import java.util.List;
import java.util.ArrayList;

public class tDT4250_asssignment1_2_Semester_Course  {

    private String Fall_or_spring;
    private boolean Mandatory;





    private tDT4250_asssignment1_2_Semester tdt4250_asssignment1_2_semester;


    public tDT4250_asssignment1_2_Semester_Course(
        String Fall_or_spring,        boolean Mandatory    ) {
        this.Fall_or_spring = Fall_or_spring;
        this.Mandatory = Mandatory;
    }


    public String getFall_or_spring() {
        return Fall_or_spring;
    }

    public void setFall_or_spring(String Fall_or_spring) {
        this.Fall_or_spring = Fall_or_spring;
    }
    public boolean getMandatory() {
        return Mandatory;
    }

    public void setMandatory(boolean Mandatory) {
        this.Mandatory = Mandatory;
    }

    public tDT4250_asssignment1_2_Semester getTdt4250_asssignment1_2_semester() {
        return tdt4250_asssignment1_2_semester;
    }

    public void setTdt4250_asssignment1_2_semester(tDT4250_asssignment1_2_Semester tdt4250_asssignment1_2_semester) {
        this.tdt4250_asssignment1_2_semester = tdt4250_asssignment1_2_semester;
    }

}