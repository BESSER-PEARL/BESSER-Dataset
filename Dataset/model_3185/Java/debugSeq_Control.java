





import java.util.List;
import java.util.ArrayList;

public class debugSeq_Control extends CodeBlock {

    private String timeout;





    private debugSeq_Expression debugseq_expression;




    private debugSeq_Expression debugseq_expression;




    private List<debugSeq_CodeBlock> debugseq_codeblocks;


    public debugSeq_Control(
        String timeout    ) {
        super(
        );
        this.timeout = timeout;
        this.debugseq_codeblocks = new ArrayList<>();
    }

    public debugSeq_Control(
        String timeout        ArrayList<debugSeq_CodeBlock> debugseq_codeblocks    ) {
        this.timeout = timeout;
        this.debugseq_codeblocks = debugseq_codeblocks;
    }

    public String getTimeout() {
        return timeout;
    }

    public void setTimeout(String timeout) {
        this.timeout = timeout;
    }

    public debugSeq_Expression getDebugseq_expression() {
        return debugseq_expression;
    }

    public void setDebugseq_expression(debugSeq_Expression debugseq_expression) {
        this.debugseq_expression = debugseq_expression;
    }
    public debugSeq_Expression getDebugseq_expression() {
        return debugseq_expression;
    }

    public void setDebugseq_expression(debugSeq_Expression debugseq_expression) {
        this.debugseq_expression = debugseq_expression;
    }
    public List<debugSeq_CodeBlock> getDebugseq_codeblocks() {
        return debugseq_codeblocks;
    }

    public void addDebugseq_codeblock(Debugseq_codeblock debugseq_codeblock) {
        this.debugseq_codeblocks.add(debugseq_codeblock);
    }

}