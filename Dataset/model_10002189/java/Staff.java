




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String education;
    private LocalDate joined;





    private Patient patient;


    public Staff(
        String education,        LocalDate joined    ) {
        this.education = education;
        this.joined = joined;
    }


    public String getEducation() {
        return education;
    }

    public void setEducation(String education) {
        this.education = education;
    }
    public LocalDate getJoined() {
        return joined;
    }

    public void setJoined(LocalDate joined) {
        this.joined = joined;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}