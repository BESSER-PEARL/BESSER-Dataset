





import java.util.List;
import java.util.ArrayList;

public class ecore_EClass extends EClassifier {

    private String interface;
    private String abstract;





    private List<EStructuralFeature> estructuralfeatures;




    private List<EStructuralFeature> estructuralfeatures;


    public ecore_EClass(
        String interface,        String abstract    ) {
        super(
        );
        this.interface = interface;
        this.abstract = abstract;
        this.estructuralfeatures = new ArrayList<>();
        this.estructuralfeatures = new ArrayList<>();
    }

    public ecore_EClass(
        String interface,        String abstract        ArrayList<EStructuralFeature> estructuralfeatures,        ArrayList<EStructuralFeature> estructuralfeatures    ) {
        this.interface = interface;
        this.abstract = abstract;
        this.estructuralfeatures = estructuralfeatures;
        this.estructuralfeatures = estructuralfeatures;
    }

    public String getInterface() {
        return interface;
    }

    public void setInterface(String interface) {
        this.interface = interface;
    }
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }

    public List<EStructuralFeature> getEstructuralfeatures() {
        return estructuralfeatures;
    }

    public void addEstructuralfeature(Estructuralfeature estructuralfeature) {
        this.estructuralfeatures.add(estructuralfeature);
    }
    public List<EStructuralFeature> getEstructuralfeatures() {
        return estructuralfeatures;
    }

    public void addEstructuralfeature(Estructuralfeature estructuralfeature) {
        this.estructuralfeatures.add(estructuralfeature);
    }

}