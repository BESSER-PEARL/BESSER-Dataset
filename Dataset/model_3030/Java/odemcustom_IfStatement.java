





import java.util.List;
import java.util.ArrayList;

public class odemcustom_IfStatement extends CompositeStatement {






    private odemcustom_Expression odemcustom_expression;




    private List<odemcustom_CodeBlock> odemcustom_codeblocks;




    private List<odemcustom_Expression> odemcustom_expressions;




    private odemcustom_CodeBlock odemcustom_codeblock;




    private odemcustom_CodeBlock odemcustom_codeblock;


    public odemcustom_IfStatement(
    ) {
        super(
        );
        this.odemcustom_codeblocks = new ArrayList<>();
        this.odemcustom_expressions = new ArrayList<>();
    }

    public odemcustom_IfStatement(
        ArrayList<odemcustom_CodeBlock> odemcustom_codeblocks,        ArrayList<odemcustom_Expression> odemcustom_expressions    ) {
        this.odemcustom_codeblocks = odemcustom_codeblocks;
        this.odemcustom_expressions = odemcustom_expressions;
    }


    public odemcustom_Expression getOdemcustom_expression() {
        return odemcustom_expression;
    }

    public void setOdemcustom_expression(odemcustom_Expression odemcustom_expression) {
        this.odemcustom_expression = odemcustom_expression;
    }
    public List<odemcustom_CodeBlock> getOdemcustom_codeblocks() {
        return odemcustom_codeblocks;
    }

    public void addOdemcustom_codeblock(Odemcustom_codeblock odemcustom_codeblock) {
        this.odemcustom_codeblocks.add(odemcustom_codeblock);
    }
    public List<odemcustom_Expression> getOdemcustom_expressions() {
        return odemcustom_expressions;
    }

    public void addOdemcustom_expression(Odemcustom_expression odemcustom_expression) {
        this.odemcustom_expressions.add(odemcustom_expression);
    }
    public odemcustom_CodeBlock getOdemcustom_codeblock() {
        return odemcustom_codeblock;
    }

    public void setOdemcustom_codeblock(odemcustom_CodeBlock odemcustom_codeblock) {
        this.odemcustom_codeblock = odemcustom_codeblock;
    }
    public odemcustom_CodeBlock getOdemcustom_codeblock() {
        return odemcustom_codeblock;
    }

    public void setOdemcustom_codeblock(odemcustom_CodeBlock odemcustom_codeblock) {
        this.odemcustom_codeblock = odemcustom_codeblock;
    }

}