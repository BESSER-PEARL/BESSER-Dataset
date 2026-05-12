





import java.util.List;
import java.util.ArrayList;

public class sml_SmlEClassifier  {

    private String name;





    private sml_TypedVariableDeclaration sml_typedvariabledeclaration;


    public sml_SmlEClassifier(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sml_TypedVariableDeclaration getSml_typedvariabledeclaration() {
        return sml_typedvariabledeclaration;
    }

    public void setSml_typedvariabledeclaration(sml_TypedVariableDeclaration sml_typedvariabledeclaration) {
        this.sml_typedvariabledeclaration = sml_typedvariabledeclaration;
    }

}