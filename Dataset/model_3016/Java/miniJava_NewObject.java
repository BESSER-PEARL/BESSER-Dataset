





import java.util.List;
import java.util.ArrayList;

public class miniJava_NewObject extends Expression {






    private miniJava_Class minijava_class;




    private List<miniJava_Expression> minijava_expressions;


    public miniJava_NewObject(
    ) {
        super(
        );
        this.minijava_expressions = new ArrayList<>();
    }

    public miniJava_NewObject(
        ArrayList<miniJava_Expression> minijava_expressions    ) {
        this.minijava_expressions = minijava_expressions;
    }


    public miniJava_Class getMinijava_class() {
        return minijava_class;
    }

    public void setMinijava_class(miniJava_Class minijava_class) {
        this.minijava_class = minijava_class;
    }
    public List<miniJava_Expression> getMinijava_expressions() {
        return minijava_expressions;
    }

    public void addMinijava_expression(Minijava_expression minijava_expression) {
        this.minijava_expressions.add(minijava_expression);
    }

}