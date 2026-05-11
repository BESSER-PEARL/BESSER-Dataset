





import java.util.List;
import java.util.ArrayList;

public class spinefm_ProcessModel_ContextManager  {

    private String fma;
    private String id;





    private MultipleSoftwareProductLine multiplesoftwareproductline;


    public spinefm_ProcessModel_ContextManager(
        String fma,        String id    ) {
        this.fma = fma;
        this.id = id;
    }


    public String getFma() {
        return fma;
    }

    public void setFma(String fma) {
        this.fma = fma;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public MultipleSoftwareProductLine getMultiplesoftwareproductline() {
        return multiplesoftwareproductline;
    }

    public void setMultiplesoftwareproductline(MultipleSoftwareProductLine multiplesoftwareproductline) {
        this.multiplesoftwareproductline = multiplesoftwareproductline;
    }

}