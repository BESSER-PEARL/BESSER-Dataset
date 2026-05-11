





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_SrcEClassifier extends SrcENamedElement {

    private String instanceClassName;
    private String instanceTypeName;





    private jointPackage_Ecore2Maude_SrcEOperation jointpackage_ecore2maude_srceoperation;


    public jointPackage_Ecore2Maude_SrcEClassifier(
        String instanceClassName,        String instanceTypeName    ) {
        super(
        );
        this.instanceClassName = instanceClassName;
        this.instanceTypeName = instanceTypeName;
    }


    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }
    public String getInstancetypename() {
        return instanceTypeName;
    }

    public void setInstancetypename(String instanceTypeName) {
        this.instanceTypeName = instanceTypeName;
    }

    public jointPackage_Ecore2Maude_SrcEOperation getJointpackage_ecore2maude_srceoperation() {
        return jointpackage_ecore2maude_srceoperation;
    }

    public void setJointpackage_ecore2maude_srceoperation(jointPackage_Ecore2Maude_SrcEOperation jointpackage_ecore2maude_srceoperation) {
        this.jointpackage_ecore2maude_srceoperation = jointpackage_ecore2maude_srceoperation;
    }

}