





import java.util.List;
import java.util.ArrayList;

public class aDSL_VariableType extends VarDef {

    private boolean isarray;





    private aDSL_XClass adsl_xclass;




    private aDSL_VariableType adsl_variabletype;


    public aDSL_VariableType(
        boolean isarray    ) {
        super(
        );
        this.isarray = isarray;
    }


    public boolean getIsarray() {
        return isarray;
    }

    public void setIsarray(boolean isarray) {
        this.isarray = isarray;
    }

    public aDSL_XClass getAdsl_xclass() {
        return adsl_xclass;
    }

    public void setAdsl_xclass(aDSL_XClass adsl_xclass) {
        this.adsl_xclass = adsl_xclass;
    }
    public aDSL_VariableType getAdsl_variabletype() {
        return adsl_variabletype;
    }

    public void setAdsl_variabletype(aDSL_VariableType adsl_variabletype) {
        this.adsl_variabletype = adsl_variabletype;
    }

}