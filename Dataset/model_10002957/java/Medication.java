




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Medication  {

    private LocalDate finish_date;
    private None drug;
    private None patient;
    private None administration;
    private int units_per_day;
    private LocalDate start_date;



    public Medication(
        LocalDate finish_date,        None drug,        None patient,        None administration,        int units_per_day,        LocalDate start_date    ) {
        this.finish_date = finish_date;
        this.drug = drug;
        this.patient = patient;
        this.administration = administration;
        this.units_per_day = units_per_day;
        this.start_date = start_date;
    }


    public LocalDate getFinish_date() {
        return finish_date;
    }

    public void setFinish_date(LocalDate finish_date) {
        this.finish_date = finish_date;
    }
    public None getDrug() {
        return drug;
    }

    public void setDrug(None drug) {
        this.drug = drug;
    }
    public None getPatient() {
        return patient;
    }

    public void setPatient(None patient) {
        this.patient = patient;
    }
    public None getAdministration() {
        return administration;
    }

    public void setAdministration(None administration) {
        this.administration = administration;
    }
    public int getUnits_per_day() {
        return units_per_day;
    }

    public void setUnits_per_day(int units_per_day) {
        this.units_per_day = units_per_day;
    }
    public LocalDate getStart_date() {
        return start_date;
    }

    public void setStart_date(LocalDate start_date) {
        this.start_date = start_date;
    }


}