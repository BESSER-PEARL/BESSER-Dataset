





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ConstructorDeclarator  {

    private String name;





    private javaDsl_ConstructorDeclaration javadsl_constructordeclaration;


    public javaDsl_ConstructorDeclarator(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public javaDsl_ConstructorDeclaration getJavadsl_constructordeclaration() {
        return javadsl_constructordeclaration;
    }

    public void setJavadsl_constructordeclaration(javaDsl_ConstructorDeclaration javadsl_constructordeclaration) {
        this.javadsl_constructordeclaration = javadsl_constructordeclaration;
    }

}