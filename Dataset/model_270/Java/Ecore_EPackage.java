





import java.util.List;
import java.util.ArrayList;

public class Ecore_EPackage extends ENamedElement {

    private String nsPrefix;
    private String nsURI;





    private List<Ecore_EPackage> ecore_epackages;




    private Ecore_EClassifier ecore_eclassifier;




    private List<Ecore_EClassifier> ecore_eclassifiers;




    private Ecore_EPackage ecore_epackage;


    public Ecore_EPackage(
        String nsPrefix,        String nsURI    ) {
        super(
        );
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.ecore_epackages = new ArrayList<>();
        this.ecore_eclassifiers = new ArrayList<>();
    }

    public Ecore_EPackage(
        String nsPrefix,        String nsURI        ArrayList<Ecore_EPackage> ecore_epackages,        ArrayList<Ecore_EClassifier> ecore_eclassifiers    ) {
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.ecore_epackages = ecore_epackages;
        this.ecore_eclassifiers = ecore_eclassifiers;
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

    public List<Ecore_EPackage> getEcore_epackages() {
        return ecore_epackages;
    }

    public void addEcore_epackage(Ecore_epackage ecore_epackage) {
        this.ecore_epackages.add(ecore_epackage);
    }
    public Ecore_EClassifier getEcore_eclassifier() {
        return ecore_eclassifier;
    }

    public void setEcore_eclassifier(Ecore_EClassifier ecore_eclassifier) {
        this.ecore_eclassifier = ecore_eclassifier;
    }
    public List<Ecore_EClassifier> getEcore_eclassifiers() {
        return ecore_eclassifiers;
    }

    public void addEcore_eclassifier(Ecore_eclassifier ecore_eclassifier) {
        this.ecore_eclassifiers.add(ecore_eclassifier);
    }
    public Ecore_EPackage getEcore_epackage() {
        return ecore_epackage;
    }

    public void setEcore_epackage(Ecore_EPackage ecore_epackage) {
        this.ecore_epackage = ecore_epackage;
    }

}