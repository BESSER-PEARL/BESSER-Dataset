





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_EPF  {

    private int id;
    private String effectve_date;
    private int precentage;



    public Class_Diagram_for_Propsed_System_EPF(
        int id,        String effectve_date,        int precentage    ) {
        this.id = id;
        this.effectve_date = effectve_date;
        this.precentage = precentage;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getEffectve_date() {
        return effectve_date;
    }

    public void setEffectve_date(String effectve_date) {
        this.effectve_date = effectve_date;
    }
    public int getPrecentage() {
        return precentage;
    }

    public void setPrecentage(int precentage) {
        this.precentage = precentage;
    }


}