





import java.util.List;
import java.util.ArrayList;

public class dbl_Expression extends ExtensibleElement, TypedElement {






    private dbl_ExpandExpression dbl_expandexpression;




    private dbl_ExpandStatement dbl_expandstatement;




    private dbl_ExpandVariablePart dbl_expandvariablepart;




    private dbl_QuotedExpression dbl_quotedexpression;




    private dbl_ExpandStatement dbl_expandstatement;




    private dbl_MetaExpr dbl_metaexpr;




    private dbl_ExpansionStatement dbl_expansionstatement;




    private dbl_CallPart dbl_callpart;


    public dbl_Expression(
    ) {
        super(
        );
    }



    public dbl_ExpandExpression getDbl_expandexpression() {
        return dbl_expandexpression;
    }

    public void setDbl_expandexpression(dbl_ExpandExpression dbl_expandexpression) {
        this.dbl_expandexpression = dbl_expandexpression;
    }
    public dbl_ExpandStatement getDbl_expandstatement() {
        return dbl_expandstatement;
    }

    public void setDbl_expandstatement(dbl_ExpandStatement dbl_expandstatement) {
        this.dbl_expandstatement = dbl_expandstatement;
    }
    public dbl_ExpandVariablePart getDbl_expandvariablepart() {
        return dbl_expandvariablepart;
    }

    public void setDbl_expandvariablepart(dbl_ExpandVariablePart dbl_expandvariablepart) {
        this.dbl_expandvariablepart = dbl_expandvariablepart;
    }
    public dbl_QuotedExpression getDbl_quotedexpression() {
        return dbl_quotedexpression;
    }

    public void setDbl_quotedexpression(dbl_QuotedExpression dbl_quotedexpression) {
        this.dbl_quotedexpression = dbl_quotedexpression;
    }
    public dbl_ExpandStatement getDbl_expandstatement() {
        return dbl_expandstatement;
    }

    public void setDbl_expandstatement(dbl_ExpandStatement dbl_expandstatement) {
        this.dbl_expandstatement = dbl_expandstatement;
    }
    public dbl_MetaExpr getDbl_metaexpr() {
        return dbl_metaexpr;
    }

    public void setDbl_metaexpr(dbl_MetaExpr dbl_metaexpr) {
        this.dbl_metaexpr = dbl_metaexpr;
    }
    public dbl_ExpansionStatement getDbl_expansionstatement() {
        return dbl_expansionstatement;
    }

    public void setDbl_expansionstatement(dbl_ExpansionStatement dbl_expansionstatement) {
        this.dbl_expansionstatement = dbl_expansionstatement;
    }
    public dbl_CallPart getDbl_callpart() {
        return dbl_callpart;
    }

    public void setDbl_callpart(dbl_CallPart dbl_callpart) {
        this.dbl_callpart = dbl_callpart;
    }

}