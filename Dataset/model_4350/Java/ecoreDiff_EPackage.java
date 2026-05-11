





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EPackage extends ENamedElement {

    private String nsPrefix;
    private String nsURI;





    private ecoreDiff_EFactory ecorediff_efactory;




    private List<ecoreDiff_EClassifier> ecorediff_eclassifiers;




    private ecoreDiff_EPackage ecorediff_epackage;




    private ecoreDiff_EPackage ecorediff_epackage;




    private ecoreDiff_EFactory ecorediff_efactory;




    private ecoreDiff_EClassifier ecorediff_eclassifier;


    public ecoreDiff_EPackage(
        String nsPrefix,        String nsURI    ) {
        super(
        );
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.ecorediff_eclassifiers = new ArrayList<>();
    }

    public ecoreDiff_EPackage(
        String nsPrefix,        String nsURI        ArrayList<ecoreDiff_EClassifier> ecorediff_eclassifiers    ) {
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.ecorediff_eclassifiers = ecorediff_eclassifiers;
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

    public ecoreDiff_EFactory getEcorediff_efactory() {
        return ecorediff_efactory;
    }

    public void setEcorediff_efactory(ecoreDiff_EFactory ecorediff_efactory) {
        this.ecorediff_efactory = ecorediff_efactory;
    }
    public List<ecoreDiff_EClassifier> getEcorediff_eclassifiers() {
        return ecorediff_eclassifiers;
    }

    public void addEcorediff_eclassifier(Ecorediff_eclassifier ecorediff_eclassifier) {
        this.ecorediff_eclassifiers.add(ecorediff_eclassifier);
    }
    public ecoreDiff_EPackage getEcorediff_epackage() {
        return ecorediff_epackage;
    }

    public void setEcorediff_epackage(ecoreDiff_EPackage ecorediff_epackage) {
        this.ecorediff_epackage = ecorediff_epackage;
    }
    public ecoreDiff_EPackage getEcorediff_epackage() {
        return ecorediff_epackage;
    }

    public void setEcorediff_epackage(ecoreDiff_EPackage ecorediff_epackage) {
        this.ecorediff_epackage = ecorediff_epackage;
    }
    public ecoreDiff_EFactory getEcorediff_efactory() {
        return ecorediff_efactory;
    }

    public void setEcorediff_efactory(ecoreDiff_EFactory ecorediff_efactory) {
        this.ecorediff_efactory = ecorediff_efactory;
    }
    public ecoreDiff_EClassifier getEcorediff_eclassifier() {
        return ecorediff_eclassifier;
    }

    public void setEcorediff_eclassifier(ecoreDiff_EClassifier ecorediff_eclassifier) {
        this.ecorediff_eclassifier = ecorediff_eclassifier;
    }

}