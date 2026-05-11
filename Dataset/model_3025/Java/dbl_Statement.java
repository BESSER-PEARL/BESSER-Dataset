





import java.util.List;
import java.util.ArrayList;

public class dbl_Statement extends ExtensibleElement {






    private dbl_ForStatement dbl_forstatement;




    private dbl_IfStatement dbl_ifstatement;




    private dbl_TargetStatement dbl_targetstatement;




    private dbl_IfStatement dbl_ifstatement;




    private dbl_QuotedStatements dbl_quotedstatements;




    private dbl_Pattern dbl_pattern;


    public dbl_Statement(
    ) {
        super(
        );
    }



    public dbl_ForStatement getDbl_forstatement() {
        return dbl_forstatement;
    }

    public void setDbl_forstatement(dbl_ForStatement dbl_forstatement) {
        this.dbl_forstatement = dbl_forstatement;
    }
    public dbl_IfStatement getDbl_ifstatement() {
        return dbl_ifstatement;
    }

    public void setDbl_ifstatement(dbl_IfStatement dbl_ifstatement) {
        this.dbl_ifstatement = dbl_ifstatement;
    }
    public dbl_TargetStatement getDbl_targetstatement() {
        return dbl_targetstatement;
    }

    public void setDbl_targetstatement(dbl_TargetStatement dbl_targetstatement) {
        this.dbl_targetstatement = dbl_targetstatement;
    }
    public dbl_IfStatement getDbl_ifstatement() {
        return dbl_ifstatement;
    }

    public void setDbl_ifstatement(dbl_IfStatement dbl_ifstatement) {
        this.dbl_ifstatement = dbl_ifstatement;
    }
    public dbl_QuotedStatements getDbl_quotedstatements() {
        return dbl_quotedstatements;
    }

    public void setDbl_quotedstatements(dbl_QuotedStatements dbl_quotedstatements) {
        this.dbl_quotedstatements = dbl_quotedstatements;
    }
    public dbl_Pattern getDbl_pattern() {
        return dbl_pattern;
    }

    public void setDbl_pattern(dbl_Pattern dbl_pattern) {
        this.dbl_pattern = dbl_pattern;
    }

}