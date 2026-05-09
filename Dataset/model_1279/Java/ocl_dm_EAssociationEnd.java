





import java.util.List;
import java.util.ArrayList;

public class ocl_dm_EAssociationEnd  {

    private String opp;
    private String mult;
    private String name;



    public ocl_dm_EAssociationEnd(
        String opp,        String mult,        String name    ) {
        this.opp = opp;
        this.mult = mult;
        this.name = name;
    }


    public String getOpp() {
        return opp;
    }

    public void setOpp(String opp) {
        this.opp = opp;
    }
    public String getMult() {
        return mult;
    }

    public void setMult(String mult) {
        this.mult = mult;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}