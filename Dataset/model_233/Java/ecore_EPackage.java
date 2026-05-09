





import java.util.List;
import java.util.ArrayList;

public class ecore_EPackage extends ENamedElement {

    private String nsPrefix;
    private String nsURI;





    private ecore_EFactory ecore_efactory;




    private List<ecore_EPackage> ecore_epackages;




    private ecore_EFactory ecore_efactory;




    private ecore_EPackage ecore_epackage;


    public ecore_EPackage(
        String nsPrefix,        String nsURI    ) {
        super(
        );
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.ecore_epackages = new ArrayList<>();
    }

    public ecore_EPackage(
        String nsPrefix,        String nsURI        ArrayList<ecore_EPackage> ecore_epackages    ) {
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.ecore_epackages = ecore_epackages;
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
    public ecore_EFactory getEcore_efactory() {
        return ecore_efactory;
    }

    public void setEcore_efactory(ecore_EFactory ecore_efactory) {
        this.ecore_efactory = ecore_efactory;
    }
    public ecore_EPackage getEcore_epackage() {
        return ecore_epackage;
    }

    public void setEcore_epackage(ecore_EPackage ecore_epackage) {
        this.ecore_epackage = ecore_epackage;
    }

}