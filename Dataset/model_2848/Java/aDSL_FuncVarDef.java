





import java.util.List;
import java.util.ArrayList;

public class aDSL_FuncVarDef extends Member, VarDef, Statement {

    private String name;





    private aDSL_VariableType adsl_variabletype;


    public aDSL_FuncVarDef(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public aDSL_VariableType getAdsl_variabletype() {
        return adsl_variabletype;
    }

    public void setAdsl_variabletype(aDSL_VariableType adsl_variabletype) {
        this.adsl_variabletype = adsl_variabletype;
    }

}