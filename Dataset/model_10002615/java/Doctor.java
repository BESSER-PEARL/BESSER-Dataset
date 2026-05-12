





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private None normal_doctor;
    private None women_doctor;
    private None dentist;



    public Doctor(
        None normal_doctor,        None women_doctor,        None dentist    ) {
        this.normal_doctor = normal_doctor;
        this.women_doctor = women_doctor;
        this.dentist = dentist;
    }


    public None getNormal_doctor() {
        return normal_doctor;
    }

    public void setNormal_doctor(None normal_doctor) {
        this.normal_doctor = normal_doctor;
    }
    public None getWomen_doctor() {
        return women_doctor;
    }

    public void setWomen_doctor(None women_doctor) {
        this.women_doctor = women_doctor;
    }
    public None getDentist() {
        return dentist;
    }

    public void setDentist(None dentist) {
        this.dentist = dentist;
    }


}