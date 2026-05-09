





import java.util.List;
import java.util.ArrayList;

public class javaDsl_InterfaceDeclaration  {

    private String name;
    private String modifiers;



    public javaDsl_InterfaceDeclaration(
        String name,        String modifiers    ) {
        this.name = name;
        this.modifiers = modifiers;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getModifiers() {
        return modifiers;
    }

    public void setModifiers(String modifiers) {
        this.modifiers = modifiers;
    }


}