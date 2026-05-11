





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_TrgParameter extends TrgModExpression {

    private String label;





    private jointPackage_Ecore2Maude_TrgModule jointpackage_ecore2maude_trgmodule;


    public jointPackage_Ecore2Maude_TrgParameter(
        String label    ) {
        super(
        );
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public jointPackage_Ecore2Maude_TrgModule getJointpackage_ecore2maude_trgmodule() {
        return jointpackage_ecore2maude_trgmodule;
    }

    public void setJointpackage_ecore2maude_trgmodule(jointPackage_Ecore2Maude_TrgModule jointpackage_ecore2maude_trgmodule) {
        this.jointpackage_ecore2maude_trgmodule = jointpackage_ecore2maude_trgmodule;
    }

}