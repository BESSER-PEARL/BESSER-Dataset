





import java.util.List;
import java.util.ArrayList;

public class java_Method_declaration  {

    private String debug;
    private String name;
    private String modifiers;



    public java_Method_declaration(
        String debug,        String name,        String modifiers    ) {
        this.debug = debug;
        this.name = name;
        this.modifiers = modifiers;
    }


    public String getDebug() {
        return debug;
    }

    public void setDebug(String debug) {
        this.debug = debug;
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