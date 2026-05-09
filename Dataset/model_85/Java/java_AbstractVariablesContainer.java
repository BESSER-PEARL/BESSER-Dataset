





import java.util.List;
import java.util.ArrayList;

public class java_AbstractVariablesContainer extends ASTNode {






    private java_TypeAccess java_typeaccess;




    private List<java_VariableDeclarationFragment> java_variabledeclarationfragments;




    private java_VariableDeclarationFragment java_variabledeclarationfragment;


    public java_AbstractVariablesContainer(
    ) {
        super(
        );
        this.java_variabledeclarationfragments = new ArrayList<>();
    }

    public java_AbstractVariablesContainer(
        ArrayList<java_VariableDeclarationFragment> java_variabledeclarationfragments    ) {
        this.java_variabledeclarationfragments = java_variabledeclarationfragments;
    }


    public java_TypeAccess getJava_typeaccess() {
        return java_typeaccess;
    }

    public void setJava_typeaccess(java_TypeAccess java_typeaccess) {
        this.java_typeaccess = java_typeaccess;
    }
    public List<java_VariableDeclarationFragment> getJava_variabledeclarationfragments() {
        return java_variabledeclarationfragments;
    }

    public void addJava_variabledeclarationfragment(Java_variabledeclarationfragment java_variabledeclarationfragment) {
        this.java_variabledeclarationfragments.add(java_variabledeclarationfragment);
    }
    public java_VariableDeclarationFragment getJava_variabledeclarationfragment() {
        return java_variabledeclarationfragment;
    }

    public void setJava_variabledeclarationfragment(java_VariableDeclarationFragment java_variabledeclarationfragment) {
        this.java_variabledeclarationfragment = java_variabledeclarationfragment;
    }

}