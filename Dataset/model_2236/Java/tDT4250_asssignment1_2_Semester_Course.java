





import java.util.List;
import java.util.ArrayList;

public class tDT4250_asssignment1_2_Semester_Course  {

    private boolean Mandatory;
    private String Fall_or_spring;



    public tDT4250_asssignment1_2_Semester_Course(
        boolean Mandatory,        String Fall_or_spring    ) {
        this.Mandatory = Mandatory;
        this.Fall_or_spring = Fall_or_spring;
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


}