





import java.util.List;
import java.util.ArrayList;

public class carnot_RoleType extends IModelParticipant {

    private int cardinality;





    private carnot_ModelType carnot_modeltype;




    private List<carnot_RoleSymbolType> carnot_rolesymboltypes;




    private carnot_OrganizationType carnot_organizationtype;




    private List<carnot_OrganizationType> carnot_organizationtypes;




    private carnot_RoleSymbolType carnot_rolesymboltype;


    public carnot_RoleType(
        int cardinality    ) {
        super(
        );
        this.cardinality = cardinality;
        this.carnot_rolesymboltypes = new ArrayList<>();
        this.carnot_organizationtypes = new ArrayList<>();
    }

    public carnot_RoleType(
        int cardinality        ArrayList<carnot_RoleSymbolType> carnot_rolesymboltypes,        ArrayList<carnot_OrganizationType> carnot_organizationtypes    ) {
        this.cardinality = cardinality;
        this.carnot_rolesymboltypes = carnot_rolesymboltypes;
        this.carnot_organizationtypes = carnot_organizationtypes;
    }

    public int getCardinality() {
        return cardinality;
    }

    public void setCardinality(int cardinality) {
        this.cardinality = cardinality;
    }

    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }
    public List<carnot_RoleSymbolType> getCarnot_rolesymboltypes() {
        return carnot_rolesymboltypes;
    }

    public void addCarnot_rolesymboltype(Carnot_rolesymboltype carnot_rolesymboltype) {
        this.carnot_rolesymboltypes.add(carnot_rolesymboltype);
    }
    public carnot_OrganizationType getCarnot_organizationtype() {
        return carnot_organizationtype;
    }

    public void setCarnot_organizationtype(carnot_OrganizationType carnot_organizationtype) {
        this.carnot_organizationtype = carnot_organizationtype;
    }
    public List<carnot_OrganizationType> getCarnot_organizationtypes() {
        return carnot_organizationtypes;
    }

    public void addCarnot_organizationtype(Carnot_organizationtype carnot_organizationtype) {
        this.carnot_organizationtypes.add(carnot_organizationtype);
    }
    public carnot_RoleSymbolType getCarnot_rolesymboltype() {
        return carnot_rolesymboltype;
    }

    public void setCarnot_rolesymboltype(carnot_RoleSymbolType carnot_rolesymboltype) {
        this.carnot_rolesymboltype = carnot_rolesymboltype;
    }

}