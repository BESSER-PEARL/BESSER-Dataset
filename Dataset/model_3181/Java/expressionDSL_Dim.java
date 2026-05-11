





import java.util.List;
import java.util.ArrayList;

public class expressionDSL_Dim  {

    private int arrayDimensions;





    private expressionDSL_ConstDef expressiondsl_constdef;




    private expressionDSL_SubFieldDef expressiondsl_subfielddef;




    private expressionDSL_StructDef expressiondsl_structdef;




    private expressionDSL_VariableDef expressiondsl_variabledef;


    public expressionDSL_Dim(
        int arrayDimensions    ) {
        this.arrayDimensions = arrayDimensions;
    }


    public int getArraydimensions() {
        return arrayDimensions;
    }

    public void setArraydimensions(int arrayDimensions) {
        this.arrayDimensions = arrayDimensions;
    }

    public expressionDSL_ConstDef getExpressiondsl_constdef() {
        return expressiondsl_constdef;
    }

    public void setExpressiondsl_constdef(expressionDSL_ConstDef expressiondsl_constdef) {
        this.expressiondsl_constdef = expressiondsl_constdef;
    }
    public expressionDSL_SubFieldDef getExpressiondsl_subfielddef() {
        return expressiondsl_subfielddef;
    }

    public void setExpressiondsl_subfielddef(expressionDSL_SubFieldDef expressiondsl_subfielddef) {
        this.expressiondsl_subfielddef = expressiondsl_subfielddef;
    }
    public expressionDSL_StructDef getExpressiondsl_structdef() {
        return expressiondsl_structdef;
    }

    public void setExpressiondsl_structdef(expressionDSL_StructDef expressiondsl_structdef) {
        this.expressiondsl_structdef = expressiondsl_structdef;
    }
    public expressionDSL_VariableDef getExpressiondsl_variabledef() {
        return expressiondsl_variabledef;
    }

    public void setExpressiondsl_variabledef(expressionDSL_VariableDef expressiondsl_variabledef) {
        this.expressiondsl_variabledef = expressiondsl_variabledef;
    }

}