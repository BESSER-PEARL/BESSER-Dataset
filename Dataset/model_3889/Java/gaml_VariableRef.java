





import java.util.List;
import java.util.ArrayList;

public class gaml_VariableRef extends Expression {






    private gaml_VarDefinition gaml_vardefinition;


    public gaml_VariableRef(
    ) {
        super(
        );
    }



    public gaml_VarDefinition getGaml_vardefinition() {
        return gaml_vardefinition;
    }

    public void setGaml_vardefinition(gaml_VarDefinition gaml_vardefinition) {
        this.gaml_vardefinition = gaml_vardefinition;
    }

}