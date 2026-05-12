




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_ETF  {

    private String precentage;
    private LocalDate effectivedate;
    private int id;



    public Class_Diagram_for_Propsed_System_ETF(
        String precentage,        LocalDate effectivedate,        int id    ) {
        this.precentage = precentage;
        this.effectivedate = effectivedate;
        this.id = id;
    }


    public String getPrecentage() {
        return precentage;
    }

    public void setPrecentage(String precentage) {
        this.precentage = precentage;
    }
    public LocalDate getEffectivedate() {
        return effectivedate;
    }

    public void setEffectivedate(LocalDate effectivedate) {
        this.effectivedate = effectivedate;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}