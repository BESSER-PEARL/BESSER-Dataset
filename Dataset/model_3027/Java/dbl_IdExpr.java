





import java.util.List;
import java.util.ArrayList;

public class dbl_IdExpr extends L1Expr {






    private dbl_ElementAccess dbl_elementaccess;




    private List<dbl_Expression> dbl_expressions;




    private dbl_TypedElement dbl_typedelement;




    private dbl_CallPart dbl_callpart;




    private dbl_ExpansionStatement dbl_expansionstatement;




    private dbl_IdExpr dbl_idexpr;




    private dbl_PredefinedId dbl_predefinedid;


    public dbl_IdExpr(
    ) {
        super(
        );
        this.dbl_expressions = new ArrayList<>();
    }

    public dbl_IdExpr(
        ArrayList<dbl_Expression> dbl_expressions    ) {
        this.dbl_expressions = dbl_expressions;
    }


    public dbl_ElementAccess getDbl_elementaccess() {
        return dbl_elementaccess;
    }

    public void setDbl_elementaccess(dbl_ElementAccess dbl_elementaccess) {
        this.dbl_elementaccess = dbl_elementaccess;
    }
    public List<dbl_Expression> getDbl_expressions() {
        return dbl_expressions;
    }

    public void addDbl_expression(Dbl_expression dbl_expression) {
        this.dbl_expressions.add(dbl_expression);
    }
    public dbl_TypedElement getDbl_typedelement() {
        return dbl_typedelement;
    }

    public void setDbl_typedelement(dbl_TypedElement dbl_typedelement) {
        this.dbl_typedelement = dbl_typedelement;
    }
    public dbl_CallPart getDbl_callpart() {
        return dbl_callpart;
    }

    public void setDbl_callpart(dbl_CallPart dbl_callpart) {
        this.dbl_callpart = dbl_callpart;
    }
    public dbl_ExpansionStatement getDbl_expansionstatement() {
        return dbl_expansionstatement;
    }

    public void setDbl_expansionstatement(dbl_ExpansionStatement dbl_expansionstatement) {
        this.dbl_expansionstatement = dbl_expansionstatement;
    }
    public dbl_IdExpr getDbl_idexpr() {
        return dbl_idexpr;
    }

    public void setDbl_idexpr(dbl_IdExpr dbl_idexpr) {
        this.dbl_idexpr = dbl_idexpr;
    }
    public dbl_PredefinedId getDbl_predefinedid() {
        return dbl_predefinedid;
    }

    public void setDbl_predefinedid(dbl_PredefinedId dbl_predefinedid) {
        this.dbl_predefinedid = dbl_predefinedid;
    }

}