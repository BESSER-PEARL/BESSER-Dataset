





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String Specialization;
    private String Shedule;



    public Doctor(
        String Specialization,        String Shedule    ) {
        this.Specialization = Specialization;
        this.Shedule = Shedule;
    }


    public String getSpecialization() {
        return Specialization;
    }

    public void setSpecialization(String Specialization) {
        this.Specialization = Specialization;
    }
    public String getShedule() {
        return Shedule;
    }

    public void setShedule(String Shedule) {
        this.Shedule = Shedule;
    }


}