





import java.util.List;
import java.util.ArrayList;

public class java_MethodRef extends ASTNode {






    private List<java_MethodRefParameter> java_methodrefparameters;


    public java_MethodRef(
    ) {
        super(
        );
        this.java_methodrefparameters = new ArrayList<>();
    }

    public java_MethodRef(
        ArrayList<java_MethodRefParameter> java_methodrefparameters    ) {
        this.java_methodrefparameters = java_methodrefparameters;
    }


    public List<java_MethodRefParameter> getJava_methodrefparameters() {
        return java_methodrefparameters;
    }

    public void addJava_methodrefparameter(Java_methodrefparameter java_methodrefparameter) {
        this.java_methodrefparameters.add(java_methodrefparameter);
    }

}