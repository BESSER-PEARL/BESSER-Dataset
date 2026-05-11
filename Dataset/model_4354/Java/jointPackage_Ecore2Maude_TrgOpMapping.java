





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_TrgOpMapping extends TrgRenMapping {

    private String to;





    private jointPackage_Ecore2Maude_TrgOperation jointpackage_ecore2maude_trgoperation;


    public jointPackage_Ecore2Maude_TrgOpMapping(
        String to    ) {
        super(
        );
        this.to = to;
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