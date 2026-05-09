





import java.util.List;
import java.util.ArrayList;

public class Java5_VariableDeclarationExpression extends Expression {






    private Java5_VariableDeclarationFragment java5_variabledeclarationfragment;




    private List<Java5_VariableDeclarationFragment> java5_variabledeclarationfragments;


    public Java5_VariableDeclarationExpression(
    ) {
        super(
        );
        this.java5_variabledeclarationfragments = new ArrayList<>();
    }

    public Java5_VariableDeclarationExpression(
        ArrayList<Java5_VariableDeclarationFragment> java5_variabledeclarationfragments    ) {
        this.java5_variabledeclarationfragments = java5_variabledeclarationfragments;
    }


    public Java5_VariableDeclarationFragment getJava5_variabledeclarationfragment() {
        return java5_variabledeclarationfragment;
    }

    public void setJava5_variabledeclarationfragment(Java5_VariableDeclarationFragment java5_variabledeclarationfragment) {
        this.java5_variabledeclarationfragment = java5_variabledeclarationfragment;
    }
    public List<Java5_VariableDeclarationFragment> getJava5_variabledeclarationfragments() {
        return java5_variabledeclarationfragments;
    }

    public void addJava5_variabledeclarationfragment(Java5_variabledeclarationfragment java5_variabledeclarationfragment) {
        this.java5_variabledeclarationfragments.add(java5_variabledeclarationfragment);
    }

}