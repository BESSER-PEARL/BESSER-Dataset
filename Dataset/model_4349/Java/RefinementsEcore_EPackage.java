





import java.util.List;
import java.util.ArrayList;

public class RefinementsEcore_EPackage extends ENamedElement {

    private String nsPrefix;
    private String nsURI;





    private RefinementsEcore_EPackage refinementsecore_epackage;




    private List<RefinementsEcore_EClassifier> refinementsecore_eclassifiers;




    private RefinementsEcore_EClassifier refinementsecore_eclassifier;




    private RefinementsEcore_EPackage refinementsecore_epackage;


    public RefinementsEcore_EPackage(
        String nsPrefix,        String nsURI    ) {
        super(
        );
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.refinementsecore_eclassifiers = new ArrayList<>();
    }

    public RefinementsEcore_EPackage(
        String nsPrefix,        String nsURI        ArrayList<RefinementsEcore_EClassifier> refinementsecore_eclassifiers    ) {
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.refinementsecore_eclassifiers = refinementsecore_eclassifiers;
    }

    public String getNsprefix() {
        return nsPrefix;
    }

    public void setNsprefix(String nsPrefix) {
        this.nsPrefix = nsPrefix;
    }
    public String getNsuri() {
        return nsURI;
    }

    public void setNsuri(String nsURI) {
        this.nsURI = nsURI;
    }

    public RefinementsEcore_EPackage getRefinementsecore_epackage() {
        return refinementsecore_epackage;
    }

    public void setRefinementsecore_epackage(RefinementsEcore_EPackage refinementsecore_epackage) {
        this.refinementsecore_epackage = refinementsecore_epackage;
    }
    public List<RefinementsEcore_EClassifier> getRefinementsecore_eclassifiers() {
        return refinementsecore_eclassifiers;
    }

    public void addRefinementsecore_eclassifier(Refinementsecore_eclassifier refinementsecore_eclassifier) {
        this.refinementsecore_eclassifiers.add(refinementsecore_eclassifier);
    }
    public RefinementsEcore_EClassifier getRefinementsecore_eclassifier() {
        return refinementsecore_eclassifier;
    }

    public void setRefinementsecore_eclassifier(RefinementsEcore_EClassifier refinementsecore_eclassifier) {
        this.refinementsecore_eclassifier = refinementsecore_eclassifier;
    }
    public RefinementsEcore_EPackage getRefinementsecore_epackage() {
        return refinementsecore_epackage;
    }

    public void setRefinementsecore_epackage(RefinementsEcore_EPackage refinementsecore_epackage) {
        this.refinementsecore_epackage = refinementsecore_epackage;
    }

}