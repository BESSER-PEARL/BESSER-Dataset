





import java.util.List;
import java.util.ArrayList;

public class aDSL_Expression extends Statement {






    private aDSL_VariableDef adsl_variabledef;




    private aDSL_ReturnStat adsl_returnstat;




    private aDSL_Operator adsl_operator;




    private aDSL_PrintInst adsl_printinst;




    private aDSL_IfStat adsl_ifstat;




    private aDSL_SharedVarDef adsl_sharedvardef;


    public aDSL_Expression(
    ) {
        super(
        );
    }



    public aDSL_VariableDef getAdsl_variabledef() {
        return adsl_variabledef;
    }

    public void setAdsl_variabledef(aDSL_VariableDef adsl_variabledef) {
        this.adsl_variabledef = adsl_variabledef;
    }
    public aDSL_ReturnStat getAdsl_returnstat() {
        return adsl_returnstat;
    }

    public void setAdsl_returnstat(aDSL_ReturnStat adsl_returnstat) {
        this.adsl_returnstat = adsl_returnstat;
    }
    public aDSL_Operator getAdsl_operator() {
        return adsl_operator;
    }

    public void setAdsl_operator(aDSL_Operator adsl_operator) {
        this.adsl_operator = adsl_operator;
    }
    public aDSL_PrintInst getAdsl_printinst() {
        return adsl_printinst;
    }

    public void setAdsl_printinst(aDSL_PrintInst adsl_printinst) {
        this.adsl_printinst = adsl_printinst;
    }
    public aDSL_IfStat getAdsl_ifstat() {
        return adsl_ifstat;
    }

    public void setAdsl_ifstat(aDSL_IfStat adsl_ifstat) {
        this.adsl_ifstat = adsl_ifstat;
    }
    public aDSL_SharedVarDef getAdsl_sharedvardef() {
        return adsl_sharedvardef;
    }

    public void setAdsl_sharedvardef(aDSL_SharedVarDef adsl_sharedvardef) {
        this.adsl_sharedvardef = adsl_sharedvardef;
    }

}