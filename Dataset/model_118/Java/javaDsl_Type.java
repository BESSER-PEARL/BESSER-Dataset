





import java.util.List;
import java.util.ArrayList;

public class javaDsl_Type  {

    private String name;





    private javaDsl_FormalParameter javadsl_formalparameter;




    private javaDsl_FieldDeclaration javadsl_fielddeclaration;


    public javaDsl_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public javaDsl_FormalParameter getJavadsl_formalparameter() {
        return javadsl_formalparameter;
    }

    public void setJavadsl_formalparameter(javaDsl_FormalParameter javadsl_formalparameter) {
        this.javadsl_formalparameter = javadsl_formalparameter;
    }
    public javaDsl_FieldDeclaration getJavadsl_fielddeclaration() {
        return javadsl_fielddeclaration;
    }

    public void setJavadsl_fielddeclaration(javaDsl_FieldDeclaration javadsl_fielddeclaration) {
        this.javadsl_fielddeclaration = javadsl_fielddeclaration;
    }

}