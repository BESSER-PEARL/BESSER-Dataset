





import java.util.List;
import java.util.ArrayList;

public class FPath_FunctionCallExp extends Expression {

    private String name;





    private List<FPath_Expression> fpath_expressions;


    public FPath_FunctionCallExp(
        String name    ) {
        super(
        );
        this.name = name;
        this.fpath_expressions = new ArrayList<>();
    }

    public FPath_FunctionCallExp(
        String name        ArrayList<FPath_Expression> fpath_expressions    ) {
        this.name = name;
        this.fpath_expressions = fpath_expressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<FPath_Expression> getFpath_expressions() {
        return fpath_expressions;
    }

    public void addFpath_expression(Fpath_expression fpath_expression) {
        this.fpath_expressions.add(fpath_expression);
    }

}