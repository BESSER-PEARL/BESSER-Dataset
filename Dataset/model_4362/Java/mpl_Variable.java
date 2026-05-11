





import java.util.List;
import java.util.ArrayList;

public class mpl_Variable  {

    private String name;





    private mpl_VariableDeclaration mpl_variabledeclaration;


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

    public mpl_VariableDeclaration getMpl_variabledeclaration() {
        return mpl_variabledeclaration;
    }

    public void setMpl_variabledeclaration(mpl_VariableDeclaration mpl_variabledeclaration) {
        this.mpl_variabledeclaration = mpl_variabledeclaration;
    }

}