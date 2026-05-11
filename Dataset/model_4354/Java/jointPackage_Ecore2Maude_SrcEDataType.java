





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_SrcEDataType extends SrcEClassifier {

    private boolean serializable;





    private jointPackage_Ecore2Maude_SrcEAttribute jointpackage_ecore2maude_srceattribute;


    public jointPackage_Ecore2Maude_SrcEDataType(
        boolean serializable    ) {
        super(
        );
        this.serializable = serializable;
    }


    public boolean getSerializable() {
        return serializable;
    }

    public void setSerializable(boolean serializable) {
        this.serializable = serializable;
    }

    public jointPackage_Ecore2Maude_SrcEAttribute getJointpackage_ecore2maude_srceattribute() {
        return jointpackage_ecore2maude_srceattribute;
    }

    public void setJointpackage_ecore2maude_srceattribute(jointPackage_Ecore2Maude_SrcEAttribute jointpackage_ecore2maude_srceattribute) {
        this.jointpackage_ecore2maude_srceattribute = jointpackage_ecore2maude_srceattribute;
    }

}