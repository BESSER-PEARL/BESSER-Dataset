





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_RelationalExpression extends BooleanExpression, BinaryExpression {

    private String redefinedOp;





    private OPLmetamodel_RelationalInit oplmetamodel_relationalinit;


    public OPLmetamodel_RelationalExpression(
        String redefinedOp    ) {
        super(
        );
        this.redefinedOp = redefinedOp;
    }


    public String getRedefinedop() {
        return redefinedOp;
    }

    public void setRedefinedop(String redefinedOp) {
        this.redefinedOp = redefinedOp;
    }

    public OPLmetamodel_RelationalInit getOplmetamodel_relationalinit() {
        return oplmetamodel_relationalinit;
    }

    public void setOplmetamodel_relationalinit(OPLmetamodel_RelationalInit oplmetamodel_relationalinit) {
        this.oplmetamodel_relationalinit = oplmetamodel_relationalinit;
    }

}