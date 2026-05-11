





import java.util.List;
import java.util.ArrayList;

public class paplj_MemberRef extends Expr {

    private boolean methodInvocation;





    private List<paplj_Expr> paplj_exprs;




    private paplj_Member paplj_member;




    private paplj_Expr paplj_expr;


    public paplj_MemberRef(
        boolean methodInvocation    ) {
        super(
        );
        this.methodInvocation = methodInvocation;
        this.paplj_exprs = new ArrayList<>();
    }

    public paplj_MemberRef(
        boolean methodInvocation        ArrayList<paplj_Expr> paplj_exprs    ) {
        this.methodInvocation = methodInvocation;
        this.paplj_exprs = paplj_exprs;
    }

    public boolean getMethodinvocation() {
        return methodInvocation;
    }

    public void setMethodinvocation(boolean methodInvocation) {
        this.methodInvocation = methodInvocation;
    }

    public List<paplj_Expr> getPaplj_exprs() {
        return paplj_exprs;
    }

    public void addPaplj_expr(Paplj_expr paplj_expr) {
        this.paplj_exprs.add(paplj_expr);
    }
    public paplj_Member getPaplj_member() {
        return paplj_member;
    }

    public void setPaplj_member(paplj_Member paplj_member) {
        this.paplj_member = paplj_member;
    }
    public paplj_Expr getPaplj_expr() {
        return paplj_expr;
    }

    public void setPaplj_expr(paplj_Expr paplj_expr) {
        this.paplj_expr = paplj_expr;
    }

}