





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_SrcEPackage extends SrcENamedElement {

    private String nsURI;
    private String nsPrefix;





    private List<jointPackage_Ecore2Maude_SrcEClassifier> jointpackage_ecore2maude_srceclassifiers;




    private jointPackage_Ecore2Maude_SrcEClassifier jointpackage_ecore2maude_srceclassifier;




    private List<jointPackage_Ecore2Maude_SrcEPackage> jointpackage_ecore2maude_srcepackages;




    private jointPackage_Ecore2Maude_SrcEPackage jointpackage_ecore2maude_srcepackage;


    public jointPackage_Ecore2Maude_SrcEPackage(
        String nsURI,        String nsPrefix    ) {
        super(
        );
        this.nsURI = nsURI;
        this.nsPrefix = nsPrefix;
        this.jointpackage_ecore2maude_srceclassifiers = new ArrayList<>();
        this.jointpackage_ecore2maude_srcepackages = new ArrayList<>();
    }

    public jointPackage_Ecore2Maude_SrcEPackage(
        String nsURI,        String nsPrefix        ArrayList<jointPackage_Ecore2Maude_SrcEClassifier> jointpackage_ecore2maude_srceclassifiers,        ArrayList<jointPackage_Ecore2Maude_SrcEPackage> jointpackage_ecore2maude_srcepackages    ) {
        this.nsURI = nsURI;
        this.nsPrefix = nsPrefix;
        this.jointpackage_ecore2maude_srceclassifiers = jointpackage_ecore2maude_srceclassifiers;
        this.jointpackage_ecore2maude_srcepackages = jointpackage_ecore2maude_srcepackages;
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

    public List<jointPackage_Ecore2Maude_SrcEClassifier> getJointpackage_ecore2maude_srceclassifiers() {
        return jointpackage_ecore2maude_srceclassifiers;
    }

    public void addJointpackage_ecore2maude_srceclassifier(Jointpackage_ecore2maude_srceclassifier jointpackage_ecore2maude_srceclassifier) {
        this.jointpackage_ecore2maude_srceclassifiers.add(jointpackage_ecore2maude_srceclassifier);
    }
    public jointPackage_Ecore2Maude_SrcEClassifier getJointpackage_ecore2maude_srceclassifier() {
        return jointpackage_ecore2maude_srceclassifier;
    }

    public void setJointpackage_ecore2maude_srceclassifier(jointPackage_Ecore2Maude_SrcEClassifier jointpackage_ecore2maude_srceclassifier) {
        this.jointpackage_ecore2maude_srceclassifier = jointpackage_ecore2maude_srceclassifier;
    }
    public List<jointPackage_Ecore2Maude_SrcEPackage> getJointpackage_ecore2maude_srcepackages() {
        return jointpackage_ecore2maude_srcepackages;
    }

    public void addJointpackage_ecore2maude_srcepackage(Jointpackage_ecore2maude_srcepackage jointpackage_ecore2maude_srcepackage) {
        this.jointpackage_ecore2maude_srcepackages.add(jointpackage_ecore2maude_srcepackage);
    }
    public jointPackage_Ecore2Maude_SrcEPackage getJointpackage_ecore2maude_srcepackage() {
        return jointpackage_ecore2maude_srcepackage;
    }

    public void setJointpackage_ecore2maude_srcepackage(jointPackage_Ecore2Maude_SrcEPackage jointpackage_ecore2maude_srcepackage) {
        this.jointpackage_ecore2maude_srcepackage = jointpackage_ecore2maude_srcepackage;
    }

}