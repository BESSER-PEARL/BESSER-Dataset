





import java.util.List;
import java.util.ArrayList;

public class debugSeq_Message extends Expression {

    private String format;





    private List<debugSeq_Parameter> debugseq_parameters;




    private debugSeq_Expression debugseq_expression;


    public debugSeq_Message(
        String format    ) {
        super(
        );
        this.format = format;
        this.debugseq_parameters = new ArrayList<>();
    }

    public debugSeq_Message(
        String format        ArrayList<debugSeq_Parameter> debugseq_parameters    ) {
        this.format = format;
        this.debugseq_parameters = debugseq_parameters;
    }

    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }

    public List<debugSeq_Parameter> getDebugseq_parameters() {
        return debugseq_parameters;
    }

    public void addDebugseq_parameter(Debugseq_parameter debugseq_parameter) {
        this.debugseq_parameters.add(debugseq_parameter);
    }
    public debugSeq_Expression getDebugseq_expression() {
        return debugseq_expression;
    }

    public void setDebugseq_expression(debugSeq_Expression debugseq_expression) {
        this.debugseq_expression = debugseq_expression;
    }

}