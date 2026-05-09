





import java.util.List;
import java.util.ArrayList;

public class morel_ForStatement extends ImperativeStatement {






    private morel_BooleanImpliesExp morel_booleanimpliesexp;




    private morel_VariableWithInit morel_variablewithinit;


    public morel_ForStatement(
    ) {
        super(
        );
    }



    public morel_BooleanImpliesExp getMorel_booleanimpliesexp() {
        return morel_booleanimpliesexp;
    }

    public void setMorel_booleanimpliesexp(morel_BooleanImpliesExp morel_booleanimpliesexp) {
        this.morel_booleanimpliesexp = morel_booleanimpliesexp;
    }
    public morel_VariableWithInit getMorel_variablewithinit() {
        return morel_variablewithinit;
    }

    public void setMorel_variablewithinit(morel_VariableWithInit morel_variablewithinit) {
        this.morel_variablewithinit = morel_variablewithinit;
    }

}