





import java.util.List;
import java.util.ArrayList;

public class ecore_EPackage extends ENamedElement {

    private String nsPrefix;
    private String nsURI;





    private ecore_EFactory ecore_efactory;




    private List<ecore_EPackage> ecore_epackages;




    private ecore_EPackage ecore_epackage;




    private ecore_EClassifier ecore_eclassifier;




    private List<ecore_EClassifier> ecore_eclassifiers;




    private ecore_EFactory ecore_efactory;


    public ecore_EPackage(
        String nsPrefix,        String nsURI    ) {
        super(
        );
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.ecore_epackages = new ArrayList<>();
        this.ecore_eclassifiers = new ArrayList<>();
    }

    public ecore_EPackage(
        String nsPrefix,        String nsURI        ArrayList<ecore_EPackage> ecore_epackages,        ArrayList<ecore_EClassifier> ecore_eclassifiers    ) {
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

    public ecore_EFactory getEcore_efactory() {
        return ecore_efactory;
    }

    public void setEcore_efactory(ecore_EFactory ecore_efactory) {
        this.ecore_efactory = ecore_efactory;
    }
    public List<ecore_EPackage> getEcore_epackages() {
        return ecore_epackages;
    }

    public void addEcore_epackage(Ecore_epackage ecore_epackage) {
        this.ecore_epackages.add(ecore_epackage);
    }
    public ecore_EPackage getEcore_epackage() {
        return ecore_epackage;
    }

    public void setEcore_epackage(ecore_EPackage ecore_epackage) {
        this.ecore_epackage = ecore_epackage;
    }
    public ecore_EClassifier getEcore_eclassifier() {
        return ecore_eclassifier;
    }

    public void setEcore_eclassifier(ecore_EClassifier ecore_eclassifier) {
        this.ecore_eclassifier = ecore_eclassifier;
    }
    public List<ecore_EClassifier> getEcore_eclassifiers() {
        return ecore_eclassifiers;
    }

    public void addEcore_eclassifier(Ecore_eclassifier ecore_eclassifier) {
        this.ecore_eclassifiers.add(ecore_eclassifier);
    }
    public ecore_EFactory getEcore_efactory() {
        return ecore_efactory;
    }

    public void setEcore_efactory(ecore_EFactory ecore_efactory) {
        this.ecore_efactory = ecore_efactory;
    }

}