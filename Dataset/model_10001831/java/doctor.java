





import java.util.List;
import java.util.ArrayList;

public class doctor  {

    private String patient;
    private String weekappointment;



    public doctor(
        String patient,        String weekappointment    ) {
        this.patient = patient;
        this.weekappointment = weekappointment;
    }


    public String getPatient() {
        return patient;
    }

    public void setPatient(String patient) {
        this.patient = patient;
    }
    public String getWeekappointment() {
        return weekappointment;
    }

    public void setWeekappointment(String weekappointment) {
        this.weekappointment = weekappointment;
    }


}