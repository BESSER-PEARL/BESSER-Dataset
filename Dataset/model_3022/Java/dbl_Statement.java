





import java.util.List;
import java.util.ArrayList;

public class dbl_Statement extends Construct {






    private dbl_QuotedStatements dbl_quotedstatements;




    private dbl_CodeBlock dbl_codeblock;


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
    public dbl_CodeBlock getDbl_codeblock() {
        return dbl_codeblock;
    }

    public void setDbl_codeblock(dbl_CodeBlock dbl_codeblock) {
        this.dbl_codeblock = dbl_codeblock;
    }

}