





import java.util.List;
import java.util.ArrayList;

public class noop_AsmStatement extends Statement {

    private String codes;





    private List<noop_Expression> noop_expressions;


    public noop_AsmStatement(
        String codes    ) {
        super(
        );
        this.codes = codes;
        this.noop_expressions = new ArrayList<>();
    }

    public noop_AsmStatement(
        String codes        ArrayList<noop_Expression> noop_expressions    ) {
        this.codes = codes;
        this.noop_expressions = noop_expressions;
    }

    public String getCodes() {
        return codes;
    }

    public void setCodes(String codes) {
        this.codes = codes;
    }

    public List<noop_Expression> getNoop_expressions() {
        return noop_expressions;
    }

    public void addNoop_expression(Noop_expression noop_expression) {
        this.noop_expressions.add(noop_expression);
    }

}