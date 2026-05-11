





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_SrcEClass extends SrcEClassifier {

    private boolean interface;
    private boolean abstract;





    private List<jointPackage_Ecore2Maude_SrcEReference> jointpackage_ecore2maude_srcereferences;




    private List<jointPackage_Ecore2Maude_SrcEOperation> jointpackage_ecore2maude_srceoperations;




    private jointPackage_Ecore2Maude_SrcEAttribute jointpackage_ecore2maude_srceattribute;




    private List<jointPackage_Ecore2Maude_SrcEAttribute> jointpackage_ecore2maude_srceattributes;




    private List<jointPackage_Ecore2Maude_SrcEOperation> jointpackage_ecore2maude_srceoperations;




    private jointPackage_Ecore2Maude_SrcEReference jointpackage_ecore2maude_srcereference;




    private jointPackage_Ecore2Maude_SrcEOperation jointpackage_ecore2maude_srceoperation;




    private List<jointPackage_Ecore2Maude_SrcEReference> jointpackage_ecore2maude_srcereferences;




    private List<jointPackage_Ecore2Maude_SrcEReference> jointpackage_ecore2maude_srcereferences;




    private jointPackage_Ecore2Maude_SrcEClass jointpackage_ecore2maude_srceclass;




    private List<jointPackage_Ecore2Maude_SrcEClass> jointpackage_ecore2maude_srceclasss;




    private List<jointPackage_Ecore2Maude_SrcEAttribute> jointpackage_ecore2maude_srceattributes;


    public jointPackage_Ecore2Maude_SrcEClass(
        boolean interface,        boolean abstract    ) {
        super(
        );
        this.interface = interface;
        this.abstract = abstract;
        this.jointpackage_ecore2maude_srcereferences = new ArrayList<>();
        this.jointpackage_ecore2maude_srceoperations = new ArrayList<>();
        this.jointpackage_ecore2maude_srceattributes = new ArrayList<>();
        this.jointpackage_ecore2maude_srceoperations = new ArrayList<>();
        this.jointpackage_ecore2maude_srcereferences = new ArrayList<>();
        this.jointpackage_ecore2maude_srcereferences = new ArrayList<>();
        this.jointpackage_ecore2maude_srceclasss = new ArrayList<>();
        this.jointpackage_ecore2maude_srceattributes = new ArrayList<>();
    }

    public jointPackage_Ecore2Maude_SrcEClass(
        boolean interface,        boolean abstract        ArrayList<jointPackage_Ecore2Maude_SrcEReference> jointpackage_ecore2maude_srcereferences,        ArrayList<jointPackage_Ecore2Maude_SrcEOperation> jointpackage_ecore2maude_srceoperations,        ArrayList<jointPackage_Ecore2Maude_SrcEAttribute> jointpackage_ecore2maude_srceattributes,        ArrayList<jointPackage_Ecore2Maude_SrcEOperation> jointpackage_ecore2maude_srceoperations,        ArrayList<jointPackage_Ecore2Maude_SrcEReference> jointpackage_ecore2maude_srcereferences,        ArrayList<jointPackage_Ecore2Maude_SrcEReference> jointpackage_ecore2maude_srcereferences,        ArrayList<jointPackage_Ecore2Maude_SrcEClass> jointpackage_ecore2maude_srceclasss,        ArrayList<jointPackage_Ecore2Maude_SrcEAttribute> jointpackage_ecore2maude_srceattributes    ) {
        this.interface = interface;
        this.abstract = abstract;
        this.jointpackage_ecore2maude_srcereferences = jointpackage_ecore2maude_srcereferences;
        this.jointpackage_ecore2maude_srceoperations = jointpackage_ecore2maude_srceoperations;
        this.jointpackage_ecore2maude_srceattributes = jointpackage_ecore2maude_srceattributes;
        this.jointpackage_ecore2maude_srceoperations = jointpackage_ecore2maude_srceoperations;
        this.jointpackage_ecore2maude_srcereferences = jointpackage_ecore2maude_srcereferences;
        this.jointpackage_ecore2maude_srcereferences = jointpackage_ecore2maude_srcereferences;
        this.jointpackage_ecore2maude_srceclasss = jointpackage_ecore2maude_srceclasss;
        this.jointpackage_ecore2maude_srceattributes = jointpackage_ecore2maude_srceattributes;
    }

    public boolean getInterface() {
        return interface;
    }

    public void setInterface(boolean interface) {
        this.interface = interface;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public List<jointPackage_Ecore2Maude_SrcEReference> getJointpackage_ecore2maude_srcereferences() {
        return jointpackage_ecore2maude_srcereferences;
    }

    public void addJointpackage_ecore2maude_srcereference(Jointpackage_ecore2maude_srcereference jointpackage_ecore2maude_srcereference) {
        this.jointpackage_ecore2maude_srcereferences.add(jointpackage_ecore2maude_srcereference);
    }
    public List<jointPackage_Ecore2Maude_SrcEOperation> getJointpackage_ecore2maude_srceoperations() {
        return jointpackage_ecore2maude_srceoperations;
    }

    public void addJointpackage_ecore2maude_srceoperation(Jointpackage_ecore2maude_srceoperation jointpackage_ecore2maude_srceoperation) {
        this.jointpackage_ecore2maude_srceoperations.add(jointpackage_ecore2maude_srceoperation);
    }
    public jointPackage_Ecore2Maude_SrcEAttribute getJointpackage_ecore2maude_srceattribute() {
        return jointpackage_ecore2maude_srceattribute;
    }

    public void setJointpackage_ecore2maude_srceattribute(jointPackage_Ecore2Maude_SrcEAttribute jointpackage_ecore2maude_srceattribute) {
        this.jointpackage_ecore2maude_srceattribute = jointpackage_ecore2maude_srceattribute;
    }
    public List<jointPackage_Ecore2Maude_SrcEAttribute> getJointpackage_ecore2maude_srceattributes() {
        return jointpackage_ecore2maude_srceattributes;
    }

    public void addJointpackage_ecore2maude_srceattribute(Jointpackage_ecore2maude_srceattribute jointpackage_ecore2maude_srceattribute) {
        this.jointpackage_ecore2maude_srceattributes.add(jointpackage_ecore2maude_srceattribute);
    }
    public List<jointPackage_Ecore2Maude_SrcEOperation> getJointpackage_ecore2maude_srceoperations() {
        return jointpackage_ecore2maude_srceoperations;
    }

    public void addJointpackage_ecore2maude_srceoperation(Jointpackage_ecore2maude_srceoperation jointpackage_ecore2maude_srceoperation) {
        this.jointpackage_ecore2maude_srceoperations.add(jointpackage_ecore2maude_srceoperation);
    }
    public jointPackage_Ecore2Maude_SrcEReference getJointpackage_ecore2maude_srcereference() {
        return jointpackage_ecore2maude_srcereference;
    }

    public void setJointpackage_ecore2maude_srcereference(jointPackage_Ecore2Maude_SrcEReference jointpackage_ecore2maude_srcereference) {
        this.jointpackage_ecore2maude_srcereference = jointpackage_ecore2maude_srcereference;
    }
    public jointPackage_Ecore2Maude_SrcEOperation getJointpackage_ecore2maude_srceoperation() {
        return jointpackage_ecore2maude_srceoperation;
    }

    public void setJointpackage_ecore2maude_srceoperation(jointPackage_Ecore2Maude_SrcEOperation jointpackage_ecore2maude_srceoperation) {
        this.jointpackage_ecore2maude_srceoperation = jointpackage_ecore2maude_srceoperation;
    }
    public List<jointPackage_Ecore2Maude_SrcEReference> getJointpackage_ecore2maude_srcereferences() {
        return jointpackage_ecore2maude_srcereferences;
    }

    public void addJointpackage_ecore2maude_srcereference(Jointpackage_ecore2maude_srcereference jointpackage_ecore2maude_srcereference) {
        this.jointpackage_ecore2maude_srcereferences.add(jointpackage_ecore2maude_srcereference);
    }
    public List<jointPackage_Ecore2Maude_SrcEReference> getJointpackage_ecore2maude_srcereferences() {
        return jointpackage_ecore2maude_srcereferences;
    }

    public void addJointpackage_ecore2maude_srcereference(Jointpackage_ecore2maude_srcereference jointpackage_ecore2maude_srcereference) {
        this.jointpackage_ecore2maude_srcereferences.add(jointpackage_ecore2maude_srcereference);
    }
    public jointPackage_Ecore2Maude_SrcEClass getJointpackage_ecore2maude_srceclass() {
        return jointpackage_ecore2maude_srceclass;
    }

    public void setJointpackage_ecore2maude_srceclass(jointPackage_Ecore2Maude_SrcEClass jointpackage_ecore2maude_srceclass) {
        this.jointpackage_ecore2maude_srceclass = jointpackage_ecore2maude_srceclass;
    }
    public List<jointPackage_Ecore2Maude_SrcEClass> getJointpackage_ecore2maude_srceclasss() {
        return jointpackage_ecore2maude_srceclasss;
    }

    public void addJointpackage_ecore2maude_srceclass(Jointpackage_ecore2maude_srceclass jointpackage_ecore2maude_srceclass) {
        this.jointpackage_ecore2maude_srceclasss.add(jointpackage_ecore2maude_srceclass);
    }
    public List<jointPackage_Ecore2Maude_SrcEAttribute> getJointpackage_ecore2maude_srceattributes() {
        return jointpackage_ecore2maude_srceattributes;
    }

    public void addJointpackage_ecore2maude_srceattribute(Jointpackage_ecore2maude_srceattribute jointpackage_ecore2maude_srceattribute) {
        this.jointpackage_ecore2maude_srceattributes.add(jointpackage_ecore2maude_srceattribute);
    }

}