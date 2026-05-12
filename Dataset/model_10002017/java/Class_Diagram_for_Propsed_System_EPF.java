





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_EPF  {

    private int id;
    private int precentage;
    private String effectve_date;



    public Class_Diagram_for_Propsed_System_EPF(
        int id,        int precentage,        String effectve_date    ) {
        this.id = id;
        this.precentage = precentage;
        this.effectve_date = effectve_date;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getPrecentage() {
        return precentage;
    }

    public void setPrecentage(int precentage) {
        this.precentage = precentage;
    }
    public String getEffectve_date() {
        return effectve_date;
    }

    public void setEffectve_date(String effectve_date) {
        this.effectve_date = effectve_date;
    }


}