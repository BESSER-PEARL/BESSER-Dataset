





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_DataDeclaration extends Declaration {

    private boolean isDecisionExpr;
    private boolean isDecisionVar;





    private OPLmetamodel_AbstractType oplmetamodel_abstracttype;


    public OPLmetamodel_DataDeclaration(
        boolean isDecisionExpr,        boolean isDecisionVar    ) {
        super(
        );
        this.isDecisionExpr = isDecisionExpr;
        this.isDecisionVar = isDecisionVar;
    }


    public boolean getIsdecisionexpr() {
        return isDecisionExpr;
    }

    public void setIsdecisionexpr(boolean isDecisionExpr) {
        this.isDecisionExpr = isDecisionExpr;
    }
    public boolean getIsdecisionvar() {
        return isDecisionVar;
    }

    public void setIsdecisionvar(boolean isDecisionVar) {
        this.isDecisionVar = isDecisionVar;
    }

    public OPLmetamodel_AbstractType getOplmetamodel_abstracttype() {
        return oplmetamodel_abstracttype;
    }

    public void setOplmetamodel_abstracttype(OPLmetamodel_AbstractType oplmetamodel_abstracttype) {
        this.oplmetamodel_abstracttype = oplmetamodel_abstracttype;
    }

}