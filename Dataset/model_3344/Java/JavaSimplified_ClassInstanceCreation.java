





import java.util.List;
import java.util.ArrayList;

public class JavaSimplified_ClassInstanceCreation extends Expression {






    private List<JavaSimplified_Expression> javasimplified_expressions;




    private JavaSimplified_Type javasimplified_type;


    public JavaSimplified_ClassInstanceCreation(
    ) {
        super(
        );
        this.javasimplified_expressions = new ArrayList<>();
    }

    public JavaSimplified_ClassInstanceCreation(
        ArrayList<JavaSimplified_Expression> javasimplified_expressions    ) {
        this.javasimplified_expressions = javasimplified_expressions;
    }


    public List<JavaSimplified_Expression> getJavasimplified_expressions() {
        return javasimplified_expressions;
    }

    public void addJavasimplified_expression(Javasimplified_expression javasimplified_expression) {
        this.javasimplified_expressions.add(javasimplified_expression);
    }
    public JavaSimplified_Type getJavasimplified_type() {
        return javasimplified_type;
    }

    public void setJavasimplified_type(JavaSimplified_Type javasimplified_type) {
        this.javasimplified_type = javasimplified_type;
    }

}