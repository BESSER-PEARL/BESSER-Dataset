





import java.util.List;
import java.util.ArrayList;

public class aadl2_PackageSection extends Namespace {

    private String noProperties;
    private String noAnnexes;





    private List<aadl2_FeatureGroupTypeRename> aadl2_featuregrouptyperenames;




    private List<aadl2_PackageRename> aadl2_packagerenames;




    private List<aadl2_AnnexLibrary> aadl2_annexlibrarys;




    private List<aadl2_ModelUnit> aadl2_modelunits;




    private List<aadl2_ComponentTypeRename> aadl2_componenttyperenames;




    private List<aadl2_Classifier> aadl2_classifiers;


    public aadl2_PackageSection(
        String noProperties,        String noAnnexes    ) {
        super(
        );
        this.noProperties = noProperties;
        this.noAnnexes = noAnnexes;
        this.aadl2_featuregrouptyperenames = new ArrayList<>();
        this.aadl2_packagerenames = new ArrayList<>();
        this.aadl2_annexlibrarys = new ArrayList<>();
        this.aadl2_modelunits = new ArrayList<>();
        this.aadl2_componenttyperenames = new ArrayList<>();
        this.aadl2_classifiers = new ArrayList<>();
    }

    public aadl2_PackageSection(
        String noProperties,        String noAnnexes        ArrayList<aadl2_FeatureGroupTypeRename> aadl2_featuregrouptyperenames,        ArrayList<aadl2_PackageRename> aadl2_packagerenames,        ArrayList<aadl2_AnnexLibrary> aadl2_annexlibrarys,        ArrayList<aadl2_ModelUnit> aadl2_modelunits,        ArrayList<aadl2_ComponentTypeRename> aadl2_componenttyperenames,        ArrayList<aadl2_Classifier> aadl2_classifiers    ) {
        this.noProperties = noProperties;
        this.noAnnexes = noAnnexes;
        this.aadl2_featuregrouptyperenames = aadl2_featuregrouptyperenames;
        this.aadl2_packagerenames = aadl2_packagerenames;
        this.aadl2_annexlibrarys = aadl2_annexlibrarys;
        this.aadl2_modelunits = aadl2_modelunits;
        this.aadl2_componenttyperenames = aadl2_componenttyperenames;
        this.aadl2_classifiers = aadl2_classifiers;
    }

    public String getNoproperties() {
        return noProperties;
    }

    public void setNoproperties(String noProperties) {
        this.noProperties = noProperties;
    }
    public String getNoannexes() {
        return noAnnexes;
    }

    public void setNoannexes(String noAnnexes) {
        this.noAnnexes = noAnnexes;
    }

    public List<aadl2_FeatureGroupTypeRename> getAadl2_featuregrouptyperenames() {
        return aadl2_featuregrouptyperenames;
    }

    public void addAadl2_featuregrouptyperename(Aadl2_featuregrouptyperename aadl2_featuregrouptyperename) {
        this.aadl2_featuregrouptyperenames.add(aadl2_featuregrouptyperename);
    }
    public List<aadl2_PackageRename> getAadl2_packagerenames() {
        return aadl2_packagerenames;
    }

    public void addAadl2_packagerename(Aadl2_packagerename aadl2_packagerename) {
        this.aadl2_packagerenames.add(aadl2_packagerename);
    }
    public List<aadl2_AnnexLibrary> getAadl2_annexlibrarys() {
        return aadl2_annexlibrarys;
    }

    public void addAadl2_annexlibrary(Aadl2_annexlibrary aadl2_annexlibrary) {
        this.aadl2_annexlibrarys.add(aadl2_annexlibrary);
    }
    public List<aadl2_ModelUnit> getAadl2_modelunits() {
        return aadl2_modelunits;
    }

    public void addAadl2_modelunit(Aadl2_modelunit aadl2_modelunit) {
        this.aadl2_modelunits.add(aadl2_modelunit);
    }
    public List<aadl2_ComponentTypeRename> getAadl2_componenttyperenames() {
        return aadl2_componenttyperenames;
    }

    public void addAadl2_componenttyperename(Aadl2_componenttyperename aadl2_componenttyperename) {
        this.aadl2_componenttyperenames.add(aadl2_componenttyperename);
    }
    public List<aadl2_Classifier> getAadl2_classifiers() {
        return aadl2_classifiers;
    }

    public void addAadl2_classifier(Aadl2_classifier aadl2_classifier) {
        this.aadl2_classifiers.add(aadl2_classifier);
    }

}