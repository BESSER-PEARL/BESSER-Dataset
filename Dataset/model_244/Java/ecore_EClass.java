





import java.util.List;
import java.util.ArrayList;

public class ecore_EClass extends EClassifier {

    private String abstract;
    private String interface;





    private List<EClass> eclasss;




    private List<EStructuralFeature> estructuralfeatures;




    private List<EStructuralFeature> estructuralfeatures;




    private List<EClass> eclasss;


    public ecore_EClass(
        String abstract,        String interface    ) {
        super(
        );
        this.abstract = abstract;
        this.interface = interface;
        this.eclasss = new ArrayList<>();
        this.estructuralfeatures = new ArrayList<>();
        this.estructuralfeatures = new ArrayList<>();
        this.eclasss = new ArrayList<>();
    }

    public ecore_EClass(
        String abstract,        String interface        ArrayList<EClass> eclasss,        ArrayList<EStructuralFeature> estructuralfeatures,        ArrayList<EStructuralFeature> estructuralfeatures,        ArrayList<EClass> eclasss    ) {
        this.abstract = abstract;
        this.interface = interface;
        this.eclasss = eclasss;
        this.estructuralfeatures = estructuralfeatures;
        this.estructuralfeatures = estructuralfeatures;
        this.eclasss = eclasss;
    }

    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }
    public String getInterface() {
        return interface;
    }

    public void setInterface(String interface) {
        this.interface = interface;
    }

    public List<EClass> getEclasss() {
        return eclasss;
    }

    public void addEclass(Eclass eclass) {
        this.eclasss.add(eclass);
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
    public List<EClass> getEclasss() {
        return eclasss;
    }

    public void addEclass(Eclass eclass) {
        this.eclasss.add(eclass);
    }

}