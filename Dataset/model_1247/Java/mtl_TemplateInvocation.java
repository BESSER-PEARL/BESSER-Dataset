





import java.util.List;
import java.util.ArrayList;

public class mtl_TemplateInvocation extends TemplateExpression {

    private boolean super;





    private List<OCLExpression> oclexpressions;




    private OCLExpression oclexpression;




    private OCLExpression oclexpression;




    private mtl_Template mtl_template;




    private OCLExpression oclexpression;


    public mtl_TemplateInvocation(
        boolean super    ) {
        super(
        );
        this.super = super;
        this.oclexpressions = new ArrayList<>();
    }

    public mtl_TemplateInvocation(
        boolean super        ArrayList<OCLExpression> oclexpressions    ) {
        this.super = super;
        this.oclexpressions = oclexpressions;
    }

    public boolean getSuper() {
        return super;
    }

    public void setSuper(boolean super) {
        this.super = super;
    }

    public List<OCLExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }
    public OCLExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OCLExpression oclexpression) {
        this.oclexpression = oclexpression;
    }
    public OCLExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OCLExpression oclexpression) {
        this.oclexpression = oclexpression;
    }
    public mtl_Template getMtl_template() {
        return mtl_template;
    }

    public void setMtl_template(mtl_Template mtl_template) {
        this.mtl_template = mtl_template;
    }
    public OCLExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OCLExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}