





import java.util.List;
import java.util.ArrayList;

public class prolog_directives_PredicateIndicator  {

    private int arity;
    private String name;



    public prolog_directives_PredicateIndicator(
        int arity,        String name    ) {
        this.arity = arity;
        this.name = name;
    }


    public int getArity() {
        return arity;
    }

    public void setArity(int arity) {
        this.arity = arity;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}