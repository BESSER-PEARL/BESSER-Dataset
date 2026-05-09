





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ClassDeclaration  {

    private String modifiers;
    private String extend;
    private String className;



    public javaDsl_ClassDeclaration(
        String modifiers,        String extend,        String className    ) {
        this.modifiers = modifiers;
        this.extend = extend;
        this.className = className;
    }


    public String getModifiers() {
        return modifiers;
    }

    public void setModifiers(String modifiers) {
        this.modifiers = modifiers;
    }
    public String getExtend() {
        return extend;
    }

    public void setExtend(String extend) {
        this.extend = extend;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }


}