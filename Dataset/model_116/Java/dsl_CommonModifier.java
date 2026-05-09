





import java.util.List;
import java.util.ArrayList;

public class dsl_CommonModifier  {

    private boolean final;
    private boolean static;
    private String visibility;
    private boolean abstract;





    private dsl_TypeDeclaration dsl_typedeclaration;


    public dsl_CommonModifier(
        boolean final,        boolean static,        String visibility,        boolean abstract    ) {
        this.final = final;
        this.static = static;
        this.visibility = visibility;
        this.abstract = abstract;
    }


    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public dsl_TypeDeclaration getDsl_typedeclaration() {
        return dsl_typedeclaration;
    }

    public void setDsl_typedeclaration(dsl_TypeDeclaration dsl_typedeclaration) {
        this.dsl_typedeclaration = dsl_typedeclaration;
    }

}