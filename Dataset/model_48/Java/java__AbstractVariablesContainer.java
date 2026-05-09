





import java.util.List;
import java.util.ArrayList;

public class java__AbstractVariablesContainer extends ASTNode {






    private java__VariableDeclarationFragment java__variabledeclarationfragment;




    private List<java__VariableDeclarationFragment> java__variabledeclarationfragments;




    private java__TypeAccess java__typeaccess;


    public java__AbstractVariablesContainer(
    ) {
        super(
        );
        this.java__variabledeclarationfragments = new ArrayList<>();
    }

    public java__AbstractVariablesContainer(
        ArrayList<java__VariableDeclarationFragment> java__variabledeclarationfragments    ) {
        this.java__variabledeclarationfragments = java__variabledeclarationfragments;
    }


    public java__VariableDeclarationFragment getJava__variabledeclarationfragment() {
        return java__variabledeclarationfragment;
    }

    public void setJava__variabledeclarationfragment(java__VariableDeclarationFragment java__variabledeclarationfragment) {
        this.java__variabledeclarationfragment = java__variabledeclarationfragment;
    }
    public List<java__VariableDeclarationFragment> getJava__variabledeclarationfragments() {
        return java__variabledeclarationfragments;
    }

    public void addJava__variabledeclarationfragment(Java__variabledeclarationfragment java__variabledeclarationfragment) {
        this.java__variabledeclarationfragments.add(java__variabledeclarationfragment);
    }
    public java__TypeAccess getJava__typeaccess() {
        return java__typeaccess;
    }

    public void setJava__typeaccess(java__TypeAccess java__typeaccess) {
        this.java__typeaccess = java__typeaccess;
    }

}