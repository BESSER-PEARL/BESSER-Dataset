





import java.util.List;
import java.util.ArrayList;

public class eTJ_MacroCall extends End, Start, ExtDate {

    private String buildin;





    private eTJ_LogicalStringLiteral etj_logicalstringliteral;




    private eTJ_Macro etj_macro;


    public eTJ_MacroCall(
        String buildin    ) {
        super(
        );
        this.buildin = buildin;
    }


    public String getBuildin() {
        return buildin;
    }

    public void setBuildin(String buildin) {
        this.buildin = buildin;
    }

    public eTJ_LogicalStringLiteral getEtj_logicalstringliteral() {
        return etj_logicalstringliteral;
    }

    public void setEtj_logicalstringliteral(eTJ_LogicalStringLiteral etj_logicalstringliteral) {
        this.etj_logicalstringliteral = etj_logicalstringliteral;
    }
    public eTJ_Macro getEtj_macro() {
        return etj_macro;
    }

    public void setEtj_macro(eTJ_Macro etj_macro) {
        this.etj_macro = etj_macro;
    }

}