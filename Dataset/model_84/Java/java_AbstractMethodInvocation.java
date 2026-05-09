





import java.util.List;
import java.util.ArrayList;

public class java_AbstractMethodInvocation extends ASTNode {






    private List<java_TypeAccess> java_typeaccesss;


    public java_AbstractMethodInvocation(
    ) {
        super(
        );
        this.java_typeaccesss = new ArrayList<>();
    }

    public java_AbstractMethodInvocation(
        ArrayList<java_TypeAccess> java_typeaccesss    ) {
        this.java_typeaccesss = java_typeaccesss;
    }


    public List<java_TypeAccess> getJava_typeaccesss() {
        return java_typeaccesss;
    }

    public void addJava_typeaccess(Java_typeaccess java_typeaccess) {
        this.java_typeaccesss.add(java_typeaccess);
    }

}