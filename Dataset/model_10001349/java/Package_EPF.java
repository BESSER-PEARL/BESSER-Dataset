





import java.util.List;
import java.util.ArrayList;

public class Package_EPF  {

    private None effectve_date;
    private int id;
    private int precentage;



    public Package_EPF(
        None effectve_date,        int id,        int precentage    ) {
        this.effectve_date = effectve_date;
        this.id = id;
        this.precentage = precentage;
    }


    public None getEffectve_date() {
        return effectve_date;
    }

    public void setEffectve_date(None effectve_date) {
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


}