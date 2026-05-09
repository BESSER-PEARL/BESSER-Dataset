





import java.util.List;
import java.util.ArrayList;

public class ecorer_EPackage extends ENamedElement {

    private String nsPrefix;
    private String nsURI;





    private ecorer_EPackage ecorer_epackage;




    private ecorer_EPackage ecorer_epackage;




    private ecorer_EFactory ecorer_efactory;




    private ecorer_EFactory ecorer_efactory;




    private List<ecorer_EClassifier> ecorer_eclassifiers;




    private ecorer_EClassifier ecorer_eclassifier;


    public ecorer_EPackage(
        String nsPrefix,        String nsURI    ) {
        super(
        );
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.ecorer_eclassifiers = new ArrayList<>();
    }

    public ecorer_EPackage(
        String nsPrefix,        String nsURI        ArrayList<ecorer_EClassifier> ecorer_eclassifiers    ) {
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.ecorer_eclassifiers = ecorer_eclassifiers;
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

    public ecorer_EPackage getEcorer_epackage() {
        return ecorer_epackage;
    }

    public void setEcorer_epackage(ecorer_EPackage ecorer_epackage) {
        this.ecorer_epackage = ecorer_epackage;
    }
    public ecorer_EPackage getEcorer_epackage() {
        return ecorer_epackage;
    }

    public void setEcorer_epackage(ecorer_EPackage ecorer_epackage) {
        this.ecorer_epackage = ecorer_epackage;
    }
    public ecorer_EFactory getEcorer_efactory() {
        return ecorer_efactory;
    }

    public void setEcorer_efactory(ecorer_EFactory ecorer_efactory) {
        this.ecorer_efactory = ecorer_efactory;
    }
    public ecorer_EFactory getEcorer_efactory() {
        return ecorer_efactory;
    }

    public void setEcorer_efactory(ecorer_EFactory ecorer_efactory) {
        this.ecorer_efactory = ecorer_efactory;
    }
    public List<ecorer_EClassifier> getEcorer_eclassifiers() {
        return ecorer_eclassifiers;
    }

    public void addEcorer_eclassifier(Ecorer_eclassifier ecorer_eclassifier) {
        this.ecorer_eclassifiers.add(ecorer_eclassifier);
    }
    public ecorer_EClassifier getEcorer_eclassifier() {
        return ecorer_eclassifier;
    }

    public void setEcorer_eclassifier(ecorer_EClassifier ecorer_eclassifier) {
        this.ecorer_eclassifier = ecorer_eclassifier;
    }

}