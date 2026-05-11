





import java.util.List;
import java.util.ArrayList;

public class aDSL_Parameter extends VarDef {

    private String name;
    private boolean istyped;





    private aDSL_VariableType adsl_variabletype;




    private aDSL_FuncVarDef adsl_funcvardef;


    public aDSL_Parameter(
        String name,        boolean istyped    ) {
        super(
        );
        this.name = name;
        this.istyped = istyped;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIstyped() {
        return istyped;
    }

    public void setIstyped(boolean istyped) {
        this.istyped = istyped;
    }

    public aDSL_VariableType getAdsl_variabletype() {
        return adsl_variabletype;
    }

    public void setAdsl_variabletype(aDSL_VariableType adsl_variabletype) {
        this.adsl_variabletype = adsl_variabletype;
    }
    public aDSL_FuncVarDef getAdsl_funcvardef() {
        return adsl_funcvardef;
    }

    public void setAdsl_funcvardef(aDSL_FuncVarDef adsl_funcvardef) {
        this.adsl_funcvardef = adsl_funcvardef;
    }

}