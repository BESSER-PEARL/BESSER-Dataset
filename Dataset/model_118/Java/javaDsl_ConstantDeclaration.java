





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ConstantDeclaration extends InterfaceMemberDeclaration {






    private javaDsl_Type javadsl_type;




    private javaDsl_VariableDeclarator javadsl_variabledeclarator;


    public javaDsl_ConstantDeclaration(
    ) {
        super(
        );
    }



    public javaDsl_Type getJavadsl_type() {
        return javadsl_type;
    }

    public void setJavadsl_type(javaDsl_Type javadsl_type) {
        this.javadsl_type = javadsl_type;
    }
    public javaDsl_VariableDeclarator getJavadsl_variabledeclarator() {
        return javadsl_variabledeclarator;
    }

    public void setJavadsl_variabledeclarator(javaDsl_VariableDeclarator javadsl_variabledeclarator) {
        this.javadsl_variabledeclarator = javadsl_variabledeclarator;
    }

}