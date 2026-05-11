





import java.util.List;
import java.util.ArrayList;

public class spinefm_MSPLModel_DEAssociation  {

    private String id;





    private List<RestrictionFunction> restrictionfunctions;




    private List<DEAssociationEnd> deassociationends;


    public spinefm_MSPLModel_DEAssociation(
        String id    ) {
        this.id = id;
        this.restrictionfunctions = new ArrayList<>();
        this.deassociationends = new ArrayList<>();
    }

    public spinefm_MSPLModel_DEAssociation(
        String id        ArrayList<RestrictionFunction> restrictionfunctions,        ArrayList<DEAssociationEnd> deassociationends    ) {
        this.id = id;
        this.restrictionfunctions = restrictionfunctions;
        this.deassociationends = deassociationends;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<RestrictionFunction> getRestrictionfunctions() {
        return restrictionfunctions;
    }

    public void addRestrictionfunction(Restrictionfunction restrictionfunction) {
        this.restrictionfunctions.add(restrictionfunction);
    }
    public List<DEAssociationEnd> getDeassociationends() {
        return deassociationends;
    }

    public void addDeassociationend(Deassociationend deassociationend) {
        this.deassociationends.add(deassociationend);
    }

}