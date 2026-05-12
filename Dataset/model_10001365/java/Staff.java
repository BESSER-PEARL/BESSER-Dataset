




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private LocalDate joined;
    private String education;





    private Patient patient;


    public Staff(
        LocalDate joined,        String education    ) {
        this.joined = joined;
        this.education = education;
    }


    public LocalDate getJoined() {
        return joined;
    }

    public void setJoined(LocalDate joined) {
        this.joined = joined;
    }
    public String getEducation() {
        return education;
    }

    public void setEducation(String education) {
        this.education = education;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}