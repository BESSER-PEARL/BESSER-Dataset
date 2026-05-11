





import java.util.List;
import java.util.ArrayList;

public class carnot_RoleType extends IModelParticipant {

    private int cardinality;





    private carnot_ModelType carnot_modeltype;




    private carnot_RoleSymbolType carnot_rolesymboltype;




    private List<carnot_RoleSymbolType> carnot_rolesymboltypes;


    public carnot_RoleType(
        int cardinality    ) {
        super(
        );
        this.cardinality = cardinality;
        this.carnot_rolesymboltypes = new ArrayList<>();
    }

    public carnot_RoleType(
        int cardinality        ArrayList<carnot_RoleSymbolType> carnot_rolesymboltypes    ) {
        this.cardinality = cardinality;
        this.carnot_rolesymboltypes = carnot_rolesymboltypes;
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
    public carnot_RoleSymbolType getCarnot_rolesymboltype() {
        return carnot_rolesymboltype;
    }

    public void setCarnot_rolesymboltype(carnot_RoleSymbolType carnot_rolesymboltype) {
        this.carnot_rolesymboltype = carnot_rolesymboltype;
    }
    public List<carnot_RoleSymbolType> getCarnot_rolesymboltypes() {
        return carnot_rolesymboltypes;
    }

    public void addCarnot_rolesymboltype(Carnot_rolesymboltype carnot_rolesymboltype) {
        this.carnot_rolesymboltypes.add(carnot_rolesymboltype);
    }

}