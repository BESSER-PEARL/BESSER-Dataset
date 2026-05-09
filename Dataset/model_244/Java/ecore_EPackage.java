





import java.util.List;
import java.util.ArrayList;

public class ecore_EPackage extends ENamedElement {

    private String nsPrefix;
    private String nsURI;





    private List<EClassifier> eclassifiers;




    private List<EPackage> epackages;




    private EPackage epackage;


    public ecore_EPackage(
        String nsPrefix,        String nsURI    ) {
        super(
        );
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.eclassifiers = new ArrayList<>();
        this.epackages = new ArrayList<>();
    }

    public ecore_EPackage(
        String nsPrefix,        String nsURI        ArrayList<EClassifier> eclassifiers,        ArrayList<EPackage> epackages    ) {
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.eclassifiers = eclassifiers;
        this.epackages = epackages;
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

    public List<EClassifier> getEclassifiers() {
        return eclassifiers;
    }

    public void addEclassifier(Eclassifier eclassifier) {
        this.eclassifiers.add(eclassifier);
    }
    public List<EPackage> getEpackages() {
        return epackages;
    }

    public void addEpackage(Epackage epackage) {
        this.epackages.add(epackage);
    }
    public EPackage getEpackage() {
        return epackage;
    }

    public void setEpackage(EPackage epackage) {
        this.epackage = epackage;
    }

}