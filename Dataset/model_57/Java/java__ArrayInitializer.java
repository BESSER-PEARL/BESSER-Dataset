





import java.util.List;
import java.util.ArrayList;

public class java__ArrayInitializer extends Expression {






    private List<java__Expression> java__expressions;


    public java__ArrayInitializer(
    ) {
        super(
        );
        this.java__expressions = new ArrayList<>();
    }

    public java__ArrayInitializer(
        ArrayList<java__Expression> java__expressions    ) {
        this.java__expressions = java__expressions;
    }


    public List<java__Expression> getJava__expressions() {
        return java__expressions;
    }

    public void addJava__expression(Java__expression java__expression) {
        this.java__expressions.add(java__expression);
    }

}