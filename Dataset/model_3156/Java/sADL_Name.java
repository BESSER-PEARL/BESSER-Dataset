





import java.util.List;
import java.util.ArrayList;

public class sADL_Name extends SadlResource {

    private boolean function;





    private List<sADL_Expression> sadl_expressions;


    public sADL_Name(
        boolean function    ) {
        super(
        );
        this.function = function;
        this.sadl_expressions = new ArrayList<>();
    }

    public sADL_Name(
        boolean function        ArrayList<sADL_Expression> sadl_expressions    ) {
        this.function = function;
        this.sadl_expressions = sadl_expressions;
    }

    public boolean getFunction() {
        return function;
    }

    public void setFunction(boolean function) {
        this.function = function;
    }

    public List<sADL_Expression> getSadl_expressions() {
        return sadl_expressions;
    }

    public void addSadl_expression(Sadl_expression sadl_expression) {
        this.sadl_expressions.add(sadl_expression);
    }

}