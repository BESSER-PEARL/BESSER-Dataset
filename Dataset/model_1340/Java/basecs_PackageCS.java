





import java.util.List;
import java.util.ArrayList;

public class basecs_PackageCS extends NamespaceCS, PackageOwnerCS {

    private String nsURI;
    private String nsPrefix;





    private List<basecs_ClassifierCS> basecs_classifiercss;




    private basecs_ClassifierCS basecs_classifiercs;


    public basecs_PackageCS(
        String nsURI,        String nsPrefix    ) {
        super(
        );
        this.nsURI = nsURI;
        this.nsPrefix = nsPrefix;
        this.basecs_classifiercss = new ArrayList<>();
    }

    public basecs_PackageCS(
        String nsURI,        String nsPrefix        ArrayList<basecs_ClassifierCS> basecs_classifiercss    ) {
        this.nsURI = nsURI;
        this.nsPrefix = nsPrefix;
        this.basecs_classifiercss = basecs_classifiercss;
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

    public List<basecs_ClassifierCS> getBasecs_classifiercss() {
        return basecs_classifiercss;
    }

    public void addBasecs_classifiercs(Basecs_classifiercs basecs_classifiercs) {
        this.basecs_classifiercss.add(basecs_classifiercs);
    }
    public basecs_ClassifierCS getBasecs_classifiercs() {
        return basecs_classifiercs;
    }

    public void setBasecs_classifiercs(basecs_ClassifierCS basecs_classifiercs) {
        this.basecs_classifiercs = basecs_classifiercs;
    }

}