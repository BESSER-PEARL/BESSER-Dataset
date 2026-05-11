





import java.util.List;
import java.util.ArrayList;

public class simpliC_Expr  {

    private String op;





    private simpliC_TFact simplic_tfact;




    private simpliC_Return simplic_return;




    private simpliC_EObject simplic_eobject;




    private List<simpliC_TFact> simplic_tfacts;




    private simpliC_Whilestmt simplic_whilestmt;




    private simpliC_Decl simplic_decl;




    private simpliC_Ifstmt simplic_ifstmt;




    private simpliC_EObject simplic_eobject;




    private simpliC_Call simplic_call;




    private simpliC_Assign simplic_assign;


    public simpliC_Expr(
        String op    ) {
        this.op = op;
        this.simplic_tfacts = new ArrayList<>();
    }

    public simpliC_Expr(
        String op        ArrayList<simpliC_TFact> simplic_tfacts    ) {
        this.op = op;
        this.simplic_tfacts = simplic_tfacts;
    }

    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public simpliC_TFact getSimplic_tfact() {
        return simplic_tfact;
    }

    public void setSimplic_tfact(simpliC_TFact simplic_tfact) {
        this.simplic_tfact = simplic_tfact;
    }
    public simpliC_Return getSimplic_return() {
        return simplic_return;
    }

    public void setSimplic_return(simpliC_Return simplic_return) {
        this.simplic_return = simplic_return;
    }
    public simpliC_EObject getSimplic_eobject() {
        return simplic_eobject;
    }

    public void setSimplic_eobject(simpliC_EObject simplic_eobject) {
        this.simplic_eobject = simplic_eobject;
    }
    public List<simpliC_TFact> getSimplic_tfacts() {
        return simplic_tfacts;
    }

    public void addSimplic_tfact(Simplic_tfact simplic_tfact) {
        this.simplic_tfacts.add(simplic_tfact);
    }
    public simpliC_Whilestmt getSimplic_whilestmt() {
        return simplic_whilestmt;
    }

    public void setSimplic_whilestmt(simpliC_Whilestmt simplic_whilestmt) {
        this.simplic_whilestmt = simplic_whilestmt;
    }
    public simpliC_Decl getSimplic_decl() {
        return simplic_decl;
    }

    public void setSimplic_decl(simpliC_Decl simplic_decl) {
        this.simplic_decl = simplic_decl;
    }
    public simpliC_Ifstmt getSimplic_ifstmt() {
        return simplic_ifstmt;
    }

    public void setSimplic_ifstmt(simpliC_Ifstmt simplic_ifstmt) {
        this.simplic_ifstmt = simplic_ifstmt;
    }
    public simpliC_EObject getSimplic_eobject() {
        return simplic_eobject;
    }

    public void setSimplic_eobject(simpliC_EObject simplic_eobject) {
        this.simplic_eobject = simplic_eobject;
    }
    public simpliC_Call getSimplic_call() {
        return simplic_call;
    }

    public void setSimplic_call(simpliC_Call simplic_call) {
        this.simplic_call = simplic_call;
    }
    public simpliC_Assign getSimplic_assign() {
        return simplic_assign;
    }

    public void setSimplic_assign(simpliC_Assign simplic_assign) {
        this.simplic_assign = simplic_assign;
    }

}