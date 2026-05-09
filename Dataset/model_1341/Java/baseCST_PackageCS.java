





import java.util.List;
import java.util.ArrayList;

public class baseCST_PackageCS extends NamespaceCS {

    private String nsPrefix;
    private String nsURI;





    private List<baseCST_PackageCS> basecst_packagecss;




    private baseCST_ClassifierCS basecst_classifiercs;




    private List<baseCST_ClassifierCS> basecst_classifiercss;


    public baseCST_PackageCS(
        String nsPrefix,        String nsURI    ) {
        super(
        );
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.basecst_packagecss = new ArrayList<>();
        this.basecst_classifiercss = new ArrayList<>();
    }

    public baseCST_PackageCS(
        String nsPrefix,        String nsURI        ArrayList<baseCST_PackageCS> basecst_packagecss,        ArrayList<baseCST_ClassifierCS> basecst_classifiercss    ) {
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.basecst_packagecss = basecst_packagecss;
        this.basecst_classifiercss = basecst_classifiercss;
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

    public List<baseCST_PackageCS> getBasecst_packagecss() {
        return basecst_packagecss;
    }

    public void addBasecst_packagecs(Basecst_packagecs basecst_packagecs) {
        this.basecst_packagecss.add(basecst_packagecs);
    }
    public baseCST_ClassifierCS getBasecst_classifiercs() {
        return basecst_classifiercs;
    }

    public void setBasecst_classifiercs(baseCST_ClassifierCS basecst_classifiercs) {
        this.basecst_classifiercs = basecst_classifiercs;
    }
    public List<baseCST_ClassifierCS> getBasecst_classifiercss() {
        return basecst_classifiercss;
    }

    public void addBasecst_classifiercs(Basecst_classifiercs basecst_classifiercs) {
        this.basecst_classifiercss.add(basecst_classifiercs);
    }

}