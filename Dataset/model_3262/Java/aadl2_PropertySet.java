





import java.util.List;
import java.util.ArrayList;

public class aadl2_PropertySet extends Namespace, ModelUnit {






    private List<aadl2_ModelUnit> aadl2_modelunits;




    private List<aadl2_AnnexSubclause> aadl2_annexsubclauses;


    public aadl2_PropertySet(
    ) {
        super(
        );
        this.aadl2_modelunits = new ArrayList<>();
        this.aadl2_annexsubclauses = new ArrayList<>();
    }

    public aadl2_PropertySet(
        ArrayList<aadl2_ModelUnit> aadl2_modelunits,        ArrayList<aadl2_AnnexSubclause> aadl2_annexsubclauses    ) {
        this.aadl2_modelunits = aadl2_modelunits;
        this.aadl2_annexsubclauses = aadl2_annexsubclauses;
    }


    public List<aadl2_ModelUnit> getAadl2_modelunits() {
        return aadl2_modelunits;
    }

    public void addAadl2_modelunit(Aadl2_modelunit aadl2_modelunit) {
        this.aadl2_modelunits.add(aadl2_modelunit);
    }
    public List<aadl2_AnnexSubclause> getAadl2_annexsubclauses() {
        return aadl2_annexsubclauses;
    }

    public void addAadl2_annexsubclause(Aadl2_annexsubclause aadl2_annexsubclause) {
        this.aadl2_annexsubclauses.add(aadl2_annexsubclause);
    }

}