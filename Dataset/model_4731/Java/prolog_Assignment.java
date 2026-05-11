





import java.util.List;
import java.util.ArrayList;

public class prolog_Assignment extends Part {






    private prolog_Term prolog_term;




    private prolog_VariableReference prolog_variablereference;


    public prolog_Assignment(
    ) {
        super(
        );
    }



    public prolog_Term getProlog_term() {
        return prolog_term;
    }

    public void setProlog_term(prolog_Term prolog_term) {
        this.prolog_term = prolog_term;
    }
    public prolog_VariableReference getProlog_variablereference() {
        return prolog_variablereference;
    }

    public void setProlog_variablereference(prolog_VariableReference prolog_variablereference) {
        this.prolog_variablereference = prolog_variablereference;
    }

}