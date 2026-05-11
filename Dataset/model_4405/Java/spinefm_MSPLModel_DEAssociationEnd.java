





import java.util.List;
import java.util.ArrayList;

public class spinefm_MSPLModel_DEAssociationEnd  {

    private String id;





    private DomainElement domainelement;




    private MultiplicityElement multiplicityelement;


    public spinefm_MSPLModel_DEAssociationEnd(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public DomainElement getDomainelement() {
        return domainelement;
    }

    public void setDomainelement(DomainElement domainelement) {
        this.domainelement = domainelement;
    }
    public MultiplicityElement getMultiplicityelement() {
        return multiplicityelement;
    }

    public void setMultiplicityelement(MultiplicityElement multiplicityelement) {
        this.multiplicityelement = multiplicityelement;
    }

}