





import java.util.List;
import java.util.ArrayList;

public class aDSL_VariableDef extends Member, VarDef, Statement {

    private String name;
    private boolean istyped;
    private boolean isinit;
    private boolean isstatic;
    private String vartype;





    private aDSL_VariableType adsl_variabletype;


    public aDSL_VariableDef(
        String name,        boolean istyped,        boolean isinit,        boolean isstatic,        String vartype    ) {
        super(
        );
        this.name = name;
        this.istyped = istyped;
        this.isinit = isinit;
        this.isstatic = isstatic;
        this.vartype = vartype;
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
    public boolean getIsinit() {
        return isinit;
    }

    public void setIsinit(boolean isinit) {
        this.isinit = isinit;
    }
    public boolean getIsstatic() {
        return isstatic;
    }

    public void setIsstatic(boolean isstatic) {
        this.isstatic = isstatic;
    }
    public String getVartype() {
        return vartype;
    }

    public void setVartype(String vartype) {
        this.vartype = vartype;
    }

    public aDSL_VariableType getAdsl_variabletype() {
        return adsl_variabletype;
    }

    public void setAdsl_variabletype(aDSL_VariableType adsl_variabletype) {
        this.adsl_variabletype = adsl_variabletype;
    }

}