





import java.util.List;
import java.util.ArrayList;

public class vcml_ConditionalStatement extends Statement {






    private vcml_Statement vcml_statement;




    private vcml_Condition vcml_condition;


    public vcml_ConditionalStatement(
    ) {
        super(
        );
    }



    public vcml_Statement getVcml_statement() {
        return vcml_statement;
    }

    public void setVcml_statement(vcml_Statement vcml_statement) {
        this.vcml_statement = vcml_statement;
    }
    public vcml_Condition getVcml_condition() {
        return vcml_condition;
    }

    public void setVcml_condition(vcml_Condition vcml_condition) {
        this.vcml_condition = vcml_condition;
    }

}