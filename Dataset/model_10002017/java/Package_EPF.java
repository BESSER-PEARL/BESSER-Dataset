





import java.util.List;
import java.util.ArrayList;

public class Package_EPF  {

    private int precentage;
    private int id;
    private None effectve_date;



    public Package_EPF(
        int precentage,        int id,        None effectve_date    ) {
        this.precentage = precentage;
        this.id = id;
        this.effectve_date = effectve_date;
    }


    public int getPrecentage() {
        return precentage;
    }

    public void setPrecentage(int precentage) {
        this.precentage = precentage;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public None getEffectve_date() {
        return effectve_date;
    }

    public void setEffectve_date(None effectve_date) {
        this.effectve_date = effectve_date;
    }


}