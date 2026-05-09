





import java.util.List;
import java.util.ArrayList;

public class java__ArrayCreation extends Expression {






    private java__TypeAccess java__typeaccess;




    private java__ArrayInitializer java__arrayinitializer;




    private List<java__Expression> java__expressions;


    public java__ArrayCreation(
    ) {
        super(
        );
        this.java__expressions = new ArrayList<>();
    }

    public java__ArrayCreation(
        ArrayList<java__Expression> java__expressions    ) {
        this.java__expressions = java__expressions;
    }


    public java__TypeAccess getJava__typeaccess() {
        return java__typeaccess;
    }

    public void setJava__typeaccess(java__TypeAccess java__typeaccess) {
        this.java__typeaccess = java__typeaccess;
    }
    public java__ArrayInitializer getJava__arrayinitializer() {
        return java__arrayinitializer;
    }

    public void setJava__arrayinitializer(java__ArrayInitializer java__arrayinitializer) {
        this.java__arrayinitializer = java__arrayinitializer;
    }
    public List<java__Expression> getJava__expressions() {
        return java__expressions;
    }

    public void addJava__expression(Java__expression java__expression) {
        this.java__expressions.add(java__expression);
    }

}