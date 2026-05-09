





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ConstructorDeclaration extends ClassBodyDeclaration {

    private String modifiers;



    public javaDsl_ConstructorDeclaration(
        String modifiers    ) {
        super(
        );
        this.modifiers = modifiers;
    }


    public String getModifiers() {
        return modifiers;
    }

    public void setModifiers(String modifiers) {
        this.modifiers = modifiers;
    }


}