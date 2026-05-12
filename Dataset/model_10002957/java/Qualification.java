




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Qualification  {

    private String type;
    private LocalDate date;
    private String institution_name;



    public Qualification(
        String type,        LocalDate date,        String institution_name    ) {
        this.type = type;
        this.date = date;
        this.institution_name = institution_name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getInstitution_name() {
        return institution_name;
    }

    public void setInstitution_name(String institution_name) {
        this.institution_name = institution_name;
    }


}