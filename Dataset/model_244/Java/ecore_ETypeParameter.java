





import java.util.List;
import java.util.ArrayList;

public class ecore_ETypeParameter extends ENamedElement {






    private List<EGenericType> egenerictypes;


    public ecore_ETypeParameter(
    ) {
        super(
        );
        this.egenerictypes = new ArrayList<>();
    }

    public ecore_ETypeParameter(
        ArrayList<EGenericType> egenerictypes    ) {
        this.egenerictypes = egenerictypes;
    }


    public List<EGenericType> getEgenerictypes() {
        return egenerictypes;
    }

    public void addEgenerictype(Egenerictype egenerictype) {
        this.egenerictypes.add(egenerictype);
    }

}