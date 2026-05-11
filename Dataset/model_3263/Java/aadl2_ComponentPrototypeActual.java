





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentPrototypeActual extends ArrayableElement {

    private String category;





    private List<aadl2_PrototypeBinding> aadl2_prototypebindings;




    private aadl2_SubcomponentType aadl2_subcomponenttype;


    public aadl2_ComponentPrototypeActual(
        String category    ) {
        super(
        );
        this.category = category;
        this.aadl2_prototypebindings = new ArrayList<>();
    }

    public aadl2_ComponentPrototypeActual(
        String category        ArrayList<aadl2_PrototypeBinding> aadl2_prototypebindings    ) {
        this.category = category;
        this.aadl2_prototypebindings = aadl2_prototypebindings;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public List<aadl2_PrototypeBinding> getAadl2_prototypebindings() {
        return aadl2_prototypebindings;
    }

    public void addAadl2_prototypebinding(Aadl2_prototypebinding aadl2_prototypebinding) {
        this.aadl2_prototypebindings.add(aadl2_prototypebinding);
    }
    public aadl2_SubcomponentType getAadl2_subcomponenttype() {
        return aadl2_subcomponenttype;
    }

    public void setAadl2_subcomponenttype(aadl2_SubcomponentType aadl2_subcomponenttype) {
        this.aadl2_subcomponenttype = aadl2_subcomponenttype;
    }

}