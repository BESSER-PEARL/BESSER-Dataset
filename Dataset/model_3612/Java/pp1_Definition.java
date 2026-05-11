





import java.util.List;
import java.util.ArrayList;

public class pp1_Definition extends Expression {

    private String className;





    private List<pp1_Expression> pp1_expressions;


    public pp1_Definition(
        String className    ) {
        super(
        );
        this.className = className;
        this.pp1_expressions = new ArrayList<>();
    }

    public pp1_Definition(
        String className        ArrayList<pp1_Expression> pp1_expressions    ) {
        this.className = className;
        this.pp1_expressions = pp1_expressions;
    }

    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }

    public List<pp1_Expression> getPp1_expressions() {
        return pp1_expressions;
    }

    public void addPp1_expression(Pp1_expression pp1_expression) {
        this.pp1_expressions.add(pp1_expression);
    }

}