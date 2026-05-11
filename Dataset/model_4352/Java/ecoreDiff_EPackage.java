





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EPackage extends ENamedElement {

    private String nsURI;
    private String nsPrefix;





    private List<ecoreDiff_EClassifier> ecorediff_eclassifiers;




    private ecoreDiff_EPackage ecorediff_epackage;




    private ecoreDiff_ChangedEPackage ecorediff_changedepackage;




    private ecoreDiff_EFactory ecorediff_efactory;




    private List<ecoreDiff_EPackage> ecorediff_epackages;


    public ecoreDiff_EPackage(
        String nsURI,        String nsPrefix    ) {
        super(
        );
        this.nsURI = nsURI;
        this.nsPrefix = nsPrefix;
        this.ecorediff_eclassifiers = new ArrayList<>();
        this.ecorediff_epackages = new ArrayList<>();
    }

    public ecoreDiff_EPackage(
        String nsURI,        String nsPrefix        ArrayList<ecoreDiff_EClassifier> ecorediff_eclassifiers,        ArrayList<ecoreDiff_EPackage> ecorediff_epackages    ) {
        this.nsURI = nsURI;
        this.nsPrefix = nsPrefix;
        this.ecorediff_eclassifiers = ecorediff_eclassifiers;
        this.ecorediff_epackages = ecorediff_epackages;
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
    public ecoreDiff_ChangedEPackage getEcorediff_changedepackage() {
        return ecorediff_changedepackage;
    }

    public void setEcorediff_changedepackage(ecoreDiff_ChangedEPackage ecorediff_changedepackage) {
        this.ecorediff_changedepackage = ecorediff_changedepackage;
    }
    public ecoreDiff_EFactory getEcorediff_efactory() {
        return ecorediff_efactory;
    }

    public void setEcorediff_efactory(ecoreDiff_EFactory ecorediff_efactory) {
        this.ecorediff_efactory = ecorediff_efactory;
    }
    public List<ecoreDiff_EPackage> getEcorediff_epackages() {
        return ecorediff_epackages;
    }

    public void addEcorediff_epackage(Ecorediff_epackage ecorediff_epackage) {
        this.ecorediff_epackages.add(ecorediff_epackage);
    }

}