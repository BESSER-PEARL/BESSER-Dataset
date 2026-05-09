





import java.util.List;
import java.util.ArrayList;

public class ocl_dm_EAssociationEnd  {

    private String name;
    private String mult;





    private EAssociationEnd eassociationend;


    public ocl_dm_EAssociationEnd(
        String name,        String mult    ) {
        this.name = name;
        this.mult = mult;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMult() {
        return mult;
    }

    public void setMult(String mult) {
        this.mult = mult;
    }

    public EAssociationEnd getEassociationend() {
        return eassociationend;
    }

    public void setEassociationend(EAssociationEnd eassociationend) {
        this.eassociationend = eassociationend;
    }

}