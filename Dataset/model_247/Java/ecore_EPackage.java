





import java.util.List;
import java.util.ArrayList;

public class ecore_EPackage extends ENamedElement {

    private String nsPrefix;
    private String nsURI;





    private List<ecore_EClass> ecore_eclasss;




    private ecore_EPackage ecore_epackage;




    private ecore_EFactory ecore_efactory;




    private ecore_EClass ecore_eclass;




    private List<ecore_EPackage> ecore_epackages;




    private ecore_EFactory ecore_efactory;


    public ecore_EPackage(
        String nsPrefix,        String nsURI    ) {
        super(
        );
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.ecore_eclasss = new ArrayList<>();
        this.ecore_epackages = new ArrayList<>();
    }

    public ecore_EPackage(
        String nsPrefix,        String nsURI        ArrayList<ecore_EClass> ecore_eclasss,        ArrayList<ecore_EPackage> ecore_epackages    ) {
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.ecore_eclasss = ecore_eclasss;
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

    public List<ecore_EClass> getEcore_eclasss() {
        return ecore_eclasss;
    }

    public void addEcore_eclass(Ecore_eclass ecore_eclass) {
        this.ecore_eclasss.add(ecore_eclass);
    }
    public ecore_EPackage getEcore_epackage() {
        return ecore_epackage;
    }

    public void setEcore_epackage(ecore_EPackage ecore_epackage) {
        this.ecore_epackage = ecore_epackage;
    }
    public ecore_EFactory getEcore_efactory() {
        return ecore_efactory;
    }

    public void setEcore_efactory(ecore_EFactory ecore_efactory) {
        this.ecore_efactory = ecore_efactory;
    }
    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
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

}