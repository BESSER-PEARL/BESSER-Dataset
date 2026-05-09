





import java.util.List;
import java.util.ArrayList;

public class javaMM_ArrayCreation extends Expression {






    private List<javaMM_Expression> javamm_expressions;




    private javaMM_ArrayInitializer javamm_arrayinitializer;




    private javaMM_TypeAccess javamm_typeaccess;


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


    public List<javaMM_Expression> getJavamm_expressions() {
        return javamm_expressions;
    }

    public void addJavamm_expression(Javamm_expression javamm_expression) {
        this.javamm_expressions.add(javamm_expression);
    }
    public javaMM_ArrayInitializer getJavamm_arrayinitializer() {
        return javamm_arrayinitializer;
    }

    public void setJavamm_arrayinitializer(javaMM_ArrayInitializer javamm_arrayinitializer) {
        this.javamm_arrayinitializer = javamm_arrayinitializer;
    }
    public javaMM_TypeAccess getJavamm_typeaccess() {
        return javamm_typeaccess;
    }

    public void setJavamm_typeaccess(javaMM_TypeAccess javamm_typeaccess) {
        this.javamm_typeaccess = javamm_typeaccess;
    }

}