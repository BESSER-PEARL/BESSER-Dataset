





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_SrcEAttribute extends SrcEStructuralFeature {

    private boolean iD;





    private jointPackage_Ecore2Maude_SrcEReference jointpackage_ecore2maude_srcereference;


    public jointPackage_Ecore2Maude_SrcEAttribute(
        boolean iD    ) {
        super(
        );
        this.iD = iD;
    }


    public boolean getId() {
        return iD;
    }

    public void setId(boolean iD) {
        this.iD = iD;
    }

    public jointPackage_Ecore2Maude_SrcEReference getJointpackage_ecore2maude_srcereference() {
        return jointpackage_ecore2maude_srcereference;
    }

    public void setJointpackage_ecore2maude_srcereference(jointPackage_Ecore2Maude_SrcEReference jointpackage_ecore2maude_srcereference) {
        this.jointpackage_ecore2maude_srcereference = jointpackage_ecore2maude_srcereference;
    }

}