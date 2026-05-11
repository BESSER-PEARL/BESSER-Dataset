





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_SrcEPackage extends SrcENamedElement {

    private String nsPrefix;
    private String nsURI;





    private jointPackage_Ecore2Maude_SrcEPackage jointpackage_ecore2maude_srcepackage;




    private List<jointPackage_Ecore2Maude_SrcEClassifier> jointpackage_ecore2maude_srceclassifiers;




    private jointPackage_Ecore2Maude_SrcEPackage jointpackage_ecore2maude_srcepackage;




    private jointPackage_Ecore2Maude_SrcEClassifier jointpackage_ecore2maude_srceclassifier;


    public jointPackage_Ecore2Maude_SrcEPackage(
        String nsPrefix,        String nsURI    ) {
        super(
        );
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.jointpackage_ecore2maude_srceclassifiers = new ArrayList<>();
    }

    public jointPackage_Ecore2Maude_SrcEPackage(
        String nsPrefix,        String nsURI        ArrayList<jointPackage_Ecore2Maude_SrcEClassifier> jointpackage_ecore2maude_srceclassifiers    ) {
        this.nsPrefix = nsPrefix;
        this.nsURI = nsURI;
        this.jointpackage_ecore2maude_srceclassifiers = jointpackage_ecore2maude_srceclassifiers;
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

    public jointPackage_Ecore2Maude_SrcEPackage getJointpackage_ecore2maude_srcepackage() {
        return jointpackage_ecore2maude_srcepackage;
    }

    public void setJointpackage_ecore2maude_srcepackage(jointPackage_Ecore2Maude_SrcEPackage jointpackage_ecore2maude_srcepackage) {
        this.jointpackage_ecore2maude_srcepackage = jointpackage_ecore2maude_srcepackage;
    }
    public List<jointPackage_Ecore2Maude_SrcEClassifier> getJointpackage_ecore2maude_srceclassifiers() {
        return jointpackage_ecore2maude_srceclassifiers;
    }

    public void addJointpackage_ecore2maude_srceclassifier(Jointpackage_ecore2maude_srceclassifier jointpackage_ecore2maude_srceclassifier) {
        this.jointpackage_ecore2maude_srceclassifiers.add(jointpackage_ecore2maude_srceclassifier);
    }
    public jointPackage_Ecore2Maude_SrcEPackage getJointpackage_ecore2maude_srcepackage() {
        return jointpackage_ecore2maude_srcepackage;
    }

    public void setJointpackage_ecore2maude_srcepackage(jointPackage_Ecore2Maude_SrcEPackage jointpackage_ecore2maude_srcepackage) {
        this.jointpackage_ecore2maude_srcepackage = jointpackage_ecore2maude_srcepackage;
    }
    public jointPackage_Ecore2Maude_SrcEClassifier getJointpackage_ecore2maude_srceclassifier() {
        return jointpackage_ecore2maude_srceclassifier;
    }

    public void setJointpackage_ecore2maude_srceclassifier(jointPackage_Ecore2Maude_SrcEClassifier jointpackage_ecore2maude_srceclassifier) {
        this.jointpackage_ecore2maude_srceclassifier = jointpackage_ecore2maude_srceclassifier;
    }

}