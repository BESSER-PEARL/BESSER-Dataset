





import java.util.List;
import java.util.ArrayList;

public class miniJava_NewObject extends Expression {






    private List<miniJava_Expression> minijava_expressions;




    private miniJava_Clazz minijava_clazz;


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


    public List<miniJava_Expression> getMinijava_expressions() {
        return minijava_expressions;
    }

    public void addMinijava_expression(Minijava_expression minijava_expression) {
        this.minijava_expressions.add(minijava_expression);
    }
    public miniJava_Clazz getMinijava_clazz() {
        return minijava_clazz;
    }

    public void setMinijava_clazz(miniJava_Clazz minijava_clazz) {
        this.minijava_clazz = minijava_clazz;
    }

}