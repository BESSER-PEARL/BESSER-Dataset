





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_ETF  {

    private int id;
    private String precentage;
    private String effectivedate;



    public Class_Diagram_for_Propsed_System_ETF(
        int id,        String precentage,        String effectivedate    ) {
        this.id = id;
        this.precentage = precentage;
        this.effectivedate = effectivedate;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getPrecentage() {
        return precentage;
    }

    public void setPrecentage(String precentage) {
        this.precentage = precentage;
    }
    public String getEffectivedate() {
        return effectivedate;
    }

    public void setEffectivedate(String effectivedate) {
        this.effectivedate = effectivedate;
    }


}