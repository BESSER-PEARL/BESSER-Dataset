





import java.util.List;
import java.util.ArrayList;

public class javaDsl_FieldDeclaration  {

    private String modifiers;





    private javaDsl_ClassMemberDeclaration javadsl_classmemberdeclaration;


    public javaDsl_FieldDeclaration(
        String modifiers    ) {
        this.modifiers = modifiers;
    }


    public String getModifiers() {
        return modifiers;
    }

    public void setModifiers(String modifiers) {
        this.modifiers = modifiers;
    }

    public javaDsl_ClassMemberDeclaration getJavadsl_classmemberdeclaration() {
        return javadsl_classmemberdeclaration;
    }

    public void setJavadsl_classmemberdeclaration(javaDsl_ClassMemberDeclaration javadsl_classmemberdeclaration) {
        this.javadsl_classmemberdeclaration = javadsl_classmemberdeclaration;
    }

}