





import java.util.List;
import java.util.ArrayList;

public class gastm_LabeledStatement extends Statement {






    private gastm_Statement gastm_statement;




    private gastm_LabelDefinition gastm_labeldefinition;


    public gastm_LabeledStatement(
    ) {
        super(
        );
    }



    public gastm_Statement getGastm_statement() {
        return gastm_statement;
    }

    public void setGastm_statement(gastm_Statement gastm_statement) {
        this.gastm_statement = gastm_statement;
    }
    public gastm_LabelDefinition getGastm_labeldefinition() {
        return gastm_labeldefinition;
    }

    public void setGastm_labeldefinition(gastm_LabelDefinition gastm_labeldefinition) {
        this.gastm_labeldefinition = gastm_labeldefinition;
    }

}