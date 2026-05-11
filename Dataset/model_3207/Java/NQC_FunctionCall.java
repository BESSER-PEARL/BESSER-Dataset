





import java.util.List;
import java.util.ArrayList;

public class NQC_FunctionCall extends CallStatement {






    private NQC_Function nqc_function;




    private List<NQC_Expression> nqc_expressions;


    public NQC_FunctionCall(
    ) {
        super(
        );
        this.nqc_expressions = new ArrayList<>();
    }

    public NQC_FunctionCall(
        ArrayList<NQC_Expression> nqc_expressions    ) {
        this.nqc_expressions = nqc_expressions;
    }


    public NQC_Function getNqc_function() {
        return nqc_function;
    }

    public void setNqc_function(NQC_Function nqc_function) {
        this.nqc_function = nqc_function;
    }
    public List<NQC_Expression> getNqc_expressions() {
        return nqc_expressions;
    }

    public void addNqc_expression(Nqc_expression nqc_expression) {
        this.nqc_expressions.add(nqc_expression);
    }

}