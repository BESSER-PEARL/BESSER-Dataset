





import java.util.List;
import java.util.ArrayList;

public class debugSeq_Block extends CodeBlock {

    private String atomic;





    private List<debugSeq_Statement> debugseq_statements;


    public debugSeq_Block(
        String atomic    ) {
        super(
        );
        this.atomic = atomic;
        this.debugseq_statements = new ArrayList<>();
    }

    public debugSeq_Block(
        String atomic        ArrayList<debugSeq_Statement> debugseq_statements    ) {
        this.atomic = atomic;
        this.debugseq_statements = debugseq_statements;
    }

    public String getAtomic() {
        return atomic;
    }

    public void setAtomic(String atomic) {
        this.atomic = atomic;
    }

    public List<debugSeq_Statement> getDebugseq_statements() {
        return debugseq_statements;
    }

    public void addDebugseq_statement(Debugseq_statement debugseq_statement) {
        this.debugseq_statements.add(debugseq_statement);
    }

}