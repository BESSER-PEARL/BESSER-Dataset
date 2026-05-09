





import java.util.List;
import java.util.ArrayList;

public class javaMM_AbstractVariablesContainer extends ASTNode {






    private List<javaMM_VariableDeclarationFragment> javamm_variabledeclarationfragments;




    private javaMM_VariableDeclarationFragment javamm_variabledeclarationfragment;




    private javaMM_TypeAccess javamm_typeaccess;


    public javaMM_AbstractVariablesContainer(
    ) {
        super(
        );
        this.javamm_variabledeclarationfragments = new ArrayList<>();
    }

    public javaMM_AbstractVariablesContainer(
        ArrayList<javaMM_VariableDeclarationFragment> javamm_variabledeclarationfragments    ) {
        this.javamm_variabledeclarationfragments = javamm_variabledeclarationfragments;
    }


    public List<javaMM_VariableDeclarationFragment> getJavamm_variabledeclarationfragments() {
        return javamm_variabledeclarationfragments;
    }

    public void addJavamm_variabledeclarationfragment(Javamm_variabledeclarationfragment javamm_variabledeclarationfragment) {
        this.javamm_variabledeclarationfragments.add(javamm_variabledeclarationfragment);
    }
    public javaMM_VariableDeclarationFragment getJavamm_variabledeclarationfragment() {
        return javamm_variabledeclarationfragment;
    }

    public void setJavamm_variabledeclarationfragment(javaMM_VariableDeclarationFragment javamm_variabledeclarationfragment) {
        this.javamm_variabledeclarationfragment = javamm_variabledeclarationfragment;
    }
    public javaMM_TypeAccess getJavamm_typeaccess() {
        return javamm_typeaccess;
    }

    public void setJavamm_typeaccess(javaMM_TypeAccess javamm_typeaccess) {
        this.javamm_typeaccess = javamm_typeaccess;
    }

}