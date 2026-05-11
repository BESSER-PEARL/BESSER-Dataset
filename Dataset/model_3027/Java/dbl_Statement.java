





import java.util.List;
import java.util.ArrayList;

public class dbl_Statement extends ExtensibleElement, AnnotateableElement {






    private dbl_QuotedStatements dbl_quotedstatements;




    private dbl_Pattern dbl_pattern;




    private dbl_TargetStatement dbl_targetstatement;


    public dbl_Statement(
    ) {
        super(
        );
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
    public dbl_TargetStatement getDbl_targetstatement() {
        return dbl_targetstatement;
    }

    public void setDbl_targetstatement(dbl_TargetStatement dbl_targetstatement) {
        this.dbl_targetstatement = dbl_targetstatement;
    }

}