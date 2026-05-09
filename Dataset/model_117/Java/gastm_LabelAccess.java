





import java.util.List;
import java.util.ArrayList;

public class gastm_LabelAccess extends Expression {






    private gastm_BreakStatement gastm_breakstatement;




    private gastm_ContinueStatement gastm_continuestatement;




    private gastm_Name gastm_name;




    private gastm_LabelDefinition gastm_labeldefinition;


    public gastm_LabelAccess(
    ) {
        super(
        );
    }



    public gastm_BreakStatement getGastm_breakstatement() {
        return gastm_breakstatement;
    }

    public void setGastm_breakstatement(gastm_BreakStatement gastm_breakstatement) {
        this.gastm_breakstatement = gastm_breakstatement;
    }
    public gastm_ContinueStatement getGastm_continuestatement() {
        return gastm_continuestatement;
    }

    public void setGastm_continuestatement(gastm_ContinueStatement gastm_continuestatement) {
        this.gastm_continuestatement = gastm_continuestatement;
    }
    public gastm_Name getGastm_name() {
        return gastm_name;
    }

    public void setGastm_name(gastm_Name gastm_name) {
        this.gastm_name = gastm_name;
    }
    public gastm_LabelDefinition getGastm_labeldefinition() {
        return gastm_labeldefinition;
    }

    public void setGastm_labeldefinition(gastm_LabelDefinition gastm_labeldefinition) {
        this.gastm_labeldefinition = gastm_labeldefinition;
    }

}