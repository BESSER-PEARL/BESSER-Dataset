





import java.util.List;
import java.util.ArrayList;

public class mpl_Variable  {

    private String name;





    private mpl_VariableReference mpl_variablereference;




    private mpl_VariableDeclaration mpl_variabledeclaration;




    private mpl_Operation mpl_operation;


    public mpl_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mpl_VariableReference getMpl_variablereference() {
        return mpl_variablereference;
    }

    public void setMpl_variablereference(mpl_VariableReference mpl_variablereference) {
        this.mpl_variablereference = mpl_variablereference;
    }
    public mpl_VariableDeclaration getMpl_variabledeclaration() {
        return mpl_variabledeclaration;
    }

    public void setMpl_variabledeclaration(mpl_VariableDeclaration mpl_variabledeclaration) {
        this.mpl_variabledeclaration = mpl_variabledeclaration;
    }
    public mpl_Operation getMpl_operation() {
        return mpl_operation;
    }

    public void setMpl_operation(mpl_Operation mpl_operation) {
        this.mpl_operation = mpl_operation;
    }

}