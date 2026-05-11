





import java.util.List;
import java.util.ArrayList;

public class dbl_IfStatement extends CompositeStatement {






    private List<dbl_CodeBlock> dbl_codeblocks;




    private dbl_CodeBlock dbl_codeblock;




    private dbl_CodeBlock dbl_codeblock;




    private List<dbl_Expression> dbl_expressions;




    private dbl_Expression dbl_expression;


    public dbl_IfStatement(
    ) {
        super(
        );
        this.dbl_codeblocks = new ArrayList<>();
        this.dbl_expressions = new ArrayList<>();
    }

    public dbl_IfStatement(
        ArrayList<dbl_CodeBlock> dbl_codeblocks,        ArrayList<dbl_Expression> dbl_expressions    ) {
        this.dbl_codeblocks = dbl_codeblocks;
        this.dbl_expressions = dbl_expressions;
    }


    public List<dbl_CodeBlock> getDbl_codeblocks() {
        return dbl_codeblocks;
    }

    public void addDbl_codeblock(Dbl_codeblock dbl_codeblock) {
        this.dbl_codeblocks.add(dbl_codeblock);
    }
    public dbl_CodeBlock getDbl_codeblock() {
        return dbl_codeblock;
    }

    public void setDbl_codeblock(dbl_CodeBlock dbl_codeblock) {
        this.dbl_codeblock = dbl_codeblock;
    }
    public dbl_CodeBlock getDbl_codeblock() {
        return dbl_codeblock;
    }

    public void setDbl_codeblock(dbl_CodeBlock dbl_codeblock) {
        this.dbl_codeblock = dbl_codeblock;
    }
    public List<dbl_Expression> getDbl_expressions() {
        return dbl_expressions;
    }

    public void addDbl_expression(Dbl_expression dbl_expression) {
        this.dbl_expressions.add(dbl_expression);
    }
    public dbl_Expression getDbl_expression() {
        return dbl_expression;
    }

    public void setDbl_expression(dbl_Expression dbl_expression) {
        this.dbl_expression = dbl_expression;
    }

}