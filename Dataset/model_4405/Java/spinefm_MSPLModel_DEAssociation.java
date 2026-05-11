





import java.util.List;
import java.util.ArrayList;

public class spinefm_MSPLModel_DEAssociation  {

    private String id;





    private DEAssociation deassociation;


    public spinefm_MSPLModel_DEAssociation(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public DEAssociation getDeassociation() {
        return deassociation;
    }

    public void setDeassociation(DEAssociation deassociation) {
        this.deassociation = deassociation;
    }

}