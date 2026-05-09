





import java.util.List;
import java.util.ArrayList;

public class javaDsl_LocalVariableDeclaration extends BlockStatement {






    private List<javaDsl_VariableDeclarator> javadsl_variabledeclarators;




    private javaDsl_Type javadsl_type;


    public javaDsl_LocalVariableDeclaration(
    ) {
        super(
        );
        this.javadsl_variabledeclarators = new ArrayList<>();
    }

    public javaDsl_LocalVariableDeclaration(
        ArrayList<javaDsl_VariableDeclarator> javadsl_variabledeclarators    ) {
        this.javadsl_variabledeclarators = javadsl_variabledeclarators;
    }


    public List<javaDsl_VariableDeclarator> getJavadsl_variabledeclarators() {
        return javadsl_variabledeclarators;
    }

    public void addJavadsl_variabledeclarator(Javadsl_variabledeclarator javadsl_variabledeclarator) {
        this.javadsl_variabledeclarators.add(javadsl_variabledeclarator);
    }
    public javaDsl_Type getJavadsl_type() {
        return javadsl_type;
    }

    public void setJavadsl_type(javaDsl_Type javadsl_type) {
        this.javadsl_type = javadsl_type;
    }

}