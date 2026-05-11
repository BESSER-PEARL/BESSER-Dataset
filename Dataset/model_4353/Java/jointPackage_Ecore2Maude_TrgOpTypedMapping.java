





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_TrgOpTypedMapping extends TrgRenMapping {

    private String atts;
    private String to;





    private jointPackage_Ecore2Maude_TrgOperation jointpackage_ecore2maude_trgoperation;


    public jointPackage_Ecore2Maude_TrgOpTypedMapping(
        String atts,        String to    ) {
        super(
        );
        this.atts = atts;
        this.to = to;
    }


    public String getAtts() {
        return atts;
    }

    public void setAtts(String atts) {
        this.atts = atts;
    }
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }

    public jointPackage_Ecore2Maude_TrgOperation getJointpackage_ecore2maude_trgoperation() {
        return jointpackage_ecore2maude_trgoperation;
    }

    public void setJointpackage_ecore2maude_trgoperation(jointPackage_Ecore2Maude_TrgOperation jointpackage_ecore2maude_trgoperation) {
        this.jointpackage_ecore2maude_trgoperation = jointpackage_ecore2maude_trgoperation;
    }

}