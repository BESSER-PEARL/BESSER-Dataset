





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_EPackage extends ENamedElement {

    private String nsPrefix;
    private String nsURI;





    private activityecorelua_EPackage activityecorelua_epackage;




    private activityecorelua_EFactory activityecorelua_efactory;




    private activityecorelua_EClassifier activityecorelua_eclassifier;




    private activityecorelua_EPackage activityecorelua_epackage;




    private activityecorelua_EFactory activityecorelua_efactory;




    private List<activityecorelua_EClassifier> activityecorelua_eclassifiers;


    public activityecorelua_EPackage(
        String nsPrefix,        String nsURI    ) {
        super(
        );
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.activityecorelua_eclassifiers = new ArrayList<>();
    }

    public activityecorelua_EPackage(
        String nsPrefix,        String nsURI        ArrayList<activityecorelua_EClassifier> activityecorelua_eclassifiers    ) {
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.activityecorelua_eclassifiers = activityecorelua_eclassifiers;
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

    public activityecorelua_EPackage getActivityecorelua_epackage() {
        return activityecorelua_epackage;
    }

    public void setActivityecorelua_epackage(activityecorelua_EPackage activityecorelua_epackage) {
        this.activityecorelua_epackage = activityecorelua_epackage;
    }
    public activityecorelua_EFactory getActivityecorelua_efactory() {
        return activityecorelua_efactory;
    }

    public void setActivityecorelua_efactory(activityecorelua_EFactory activityecorelua_efactory) {
        this.activityecorelua_efactory = activityecorelua_efactory;
    }
    public activityecorelua_EClassifier getActivityecorelua_eclassifier() {
        return activityecorelua_eclassifier;
    }

    public void setActivityecorelua_eclassifier(activityecorelua_EClassifier activityecorelua_eclassifier) {
        this.activityecorelua_eclassifier = activityecorelua_eclassifier;
    }
    public activityecorelua_EPackage getActivityecorelua_epackage() {
        return activityecorelua_epackage;
    }

    public void setActivityecorelua_epackage(activityecorelua_EPackage activityecorelua_epackage) {
        this.activityecorelua_epackage = activityecorelua_epackage;
    }
    public activityecorelua_EFactory getActivityecorelua_efactory() {
        return activityecorelua_efactory;
    }

    public void setActivityecorelua_efactory(activityecorelua_EFactory activityecorelua_efactory) {
        this.activityecorelua_efactory = activityecorelua_efactory;
    }
    public List<activityecorelua_EClassifier> getActivityecorelua_eclassifiers() {
        return activityecorelua_eclassifiers;
    }

    public void addActivityecorelua_eclassifier(Activityecorelua_eclassifier activityecorelua_eclassifier) {
        this.activityecorelua_eclassifiers.add(activityecorelua_eclassifier);
    }

}