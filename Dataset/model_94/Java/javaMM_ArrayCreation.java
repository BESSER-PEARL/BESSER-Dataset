





import java.util.List;
import java.util.ArrayList;

public class javaMM_ArrayCreation extends Expression {






    private javaMM_TypeAccess javamm_typeaccess;




    private List<javaMM_Expression> javamm_expressions;


    public javaMM_ArrayCreation(
    ) {
        super(
        );
        this.javamm_expressions = new ArrayList<>();
    }

    public javaMM_ArrayCreation(
        ArrayList<javaMM_Expression> javamm_expressions    ) {
        this.javamm_expressions = javamm_expressions;
    }


    public javaMM_TypeAccess getJavamm_typeaccess() {
        return javamm_typeaccess;
    }

    public void setJavamm_typeaccess(javaMM_TypeAccess javamm_typeaccess) {
        this.javamm_typeaccess = javamm_typeaccess;
    }
    public List<javaMM_Expression> getJavamm_expressions() {
        return javamm_expressions;
    }

    public void addJavamm_expression(Javamm_expression javamm_expression) {
        this.javamm_expressions.add(javamm_expression);
    }

}