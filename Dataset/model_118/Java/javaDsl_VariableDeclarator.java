





import java.util.List;
import java.util.ArrayList;

public class javaDsl_VariableDeclarator  {

    private String name;





    private javaDsl_VariableInitializer javadsl_variableinitializer;




    private javaDsl_FieldDeclaration javadsl_fielddeclaration;


    public javaDsl_VariableDeclarator(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public javaDsl_VariableInitializer getJavadsl_variableinitializer() {
        return javadsl_variableinitializer;
    }

    public void setJavadsl_variableinitializer(javaDsl_VariableInitializer javadsl_variableinitializer) {
        this.javadsl_variableinitializer = javadsl_variableinitializer;
    }
    public javaDsl_FieldDeclaration getJavadsl_fielddeclaration() {
        return javadsl_fielddeclaration;
    }

    public void setJavadsl_fielddeclaration(javaDsl_FieldDeclaration javadsl_fielddeclaration) {
        this.javadsl_fielddeclaration = javadsl_fielddeclaration;
    }

}