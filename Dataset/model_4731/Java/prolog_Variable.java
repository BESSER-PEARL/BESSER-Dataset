





import java.util.List;
import java.util.ArrayList;

public class prolog_Variable extends Term, Tail {

    private String name;





    private prolog_VariableReference prolog_variablereference;


    public prolog_Variable(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public prolog_VariableReference getProlog_variablereference() {
        return prolog_variablereference;
    }

    public void setProlog_variablereference(prolog_VariableReference prolog_variablereference) {
        this.prolog_variablereference = prolog_variablereference;
    }

}