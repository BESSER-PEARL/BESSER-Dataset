





import java.util.List;
import java.util.ArrayList;

public class ecoreO_EPackage extends ENamedElement {

    private String nsURI;
    private String nsPrefix;





    private ecoreO_EFactory ecoreo_efactory;




    private ecoreO_EPackage ecoreo_epackage;




    private List<ecoreO_EClassifier> ecoreo_eclassifiers;




    private ecoreO_EFactory ecoreo_efactory;




    private ecoreO_EClassifier ecoreo_eclassifier;




    private ecoreO_EPackage ecoreo_epackage;


    public ecoreO_EPackage(
        String nsURI,        String nsPrefix    ) {
        super(
        );
        this.nsURI = nsURI;
        this.nsPrefix = nsPrefix;
        this.ecoreo_eclassifiers = new ArrayList<>();
    }

    public ecoreO_EPackage(
        String nsURI,        String nsPrefix        ArrayList<ecoreO_EClassifier> ecoreo_eclassifiers    ) {
        this.nsURI = nsURI;
        this.nsPrefix = nsPrefix;
        this.ecoreo_eclassifiers = ecoreo_eclassifiers;
    }

    public String getNsuri() {
        return nsURI;
    }

    public void setNsuri(String nsURI) {
        this.nsURI = nsURI;
    }
    public String getNsprefix() {
        return nsPrefix;
    }

    public void setNsprefix(String nsPrefix) {
        this.nsPrefix = nsPrefix;
    }

    public ecoreO_EFactory getEcoreo_efactory() {
        return ecoreo_efactory;
    }

    public void setEcoreo_efactory(ecoreO_EFactory ecoreo_efactory) {
        this.ecoreo_efactory = ecoreo_efactory;
    }
    public ecoreO_EPackage getEcoreo_epackage() {
        return ecoreo_epackage;
    }

    public void setEcoreo_epackage(ecoreO_EPackage ecoreo_epackage) {
        this.ecoreo_epackage = ecoreo_epackage;
    }
    public List<ecoreO_EClassifier> getEcoreo_eclassifiers() {
        return ecoreo_eclassifiers;
    }

    public void addEcoreo_eclassifier(Ecoreo_eclassifier ecoreo_eclassifier) {
        this.ecoreo_eclassifiers.add(ecoreo_eclassifier);
    }
    public ecoreO_EFactory getEcoreo_efactory() {
        return ecoreo_efactory;
    }

    public void setEcoreo_efactory(ecoreO_EFactory ecoreo_efactory) {
        this.ecoreo_efactory = ecoreo_efactory;
    }
    public ecoreO_EClassifier getEcoreo_eclassifier() {
        return ecoreo_eclassifier;
    }

    public void setEcoreo_eclassifier(ecoreO_EClassifier ecoreo_eclassifier) {
        this.ecoreo_eclassifier = ecoreo_eclassifier;
    }
    public ecoreO_EPackage getEcoreo_epackage() {
        return ecoreo_epackage;
    }

    public void setEcoreo_epackage(ecoreO_EPackage ecoreo_epackage) {
        this.ecoreo_epackage = ecoreo_epackage;
    }

}