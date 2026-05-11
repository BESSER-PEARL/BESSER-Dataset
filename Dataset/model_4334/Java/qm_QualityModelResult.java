




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class qm_QualityModelResult  {

    private LocalDate date;
    private String system;



    public qm_QualityModelResult(
        LocalDate date,        String system    ) {
        this.date = date;
        this.system = system;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getSystem() {
        return system;
    }

    public void setSystem(String system) {
        this.system = system;
    }


}