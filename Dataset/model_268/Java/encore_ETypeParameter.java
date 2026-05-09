





import java.util.List;
import java.util.ArrayList;

public class encore_ETypeParameter extends ENamedElement {






    private List<encore_EGenericType> encore_egenerictypes;




    private encore_EOperation encore_eoperation;




    private encore_EGenericType encore_egenerictype;


    public encore_ETypeParameter(
    ) {
        super(
        );
        this.encore_egenerictypes = new ArrayList<>();
    }

    public encore_ETypeParameter(
        ArrayList<encore_EGenericType> encore_egenerictypes    ) {
        this.encore_egenerictypes = encore_egenerictypes;
    }


    public List<encore_EGenericType> getEncore_egenerictypes() {
        return encore_egenerictypes;
    }

    public void addEncore_egenerictype(Encore_egenerictype encore_egenerictype) {
        this.encore_egenerictypes.add(encore_egenerictype);
    }
    public encore_EOperation getEncore_eoperation() {
        return encore_eoperation;
    }

    public void setEncore_eoperation(encore_EOperation encore_eoperation) {
        this.encore_eoperation = encore_eoperation;
    }
    public encore_EGenericType getEncore_egenerictype() {
        return encore_egenerictype;
    }

    public void setEncore_egenerictype(encore_EGenericType encore_egenerictype) {
        this.encore_egenerictype = encore_egenerictype;
    }

}