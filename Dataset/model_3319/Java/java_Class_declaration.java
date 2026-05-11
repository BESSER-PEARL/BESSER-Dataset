





import java.util.List;
import java.util.ArrayList;

public class java_Class_declaration  {

    private String className;
    private String modifiers;
    private String implements;
    private String extend;
    private String implement;





    private List<java_Field_declaration> java_field_declarations;


    public java_Class_declaration(
        String className,        String modifiers,        String implements,        String extend,        String implement    ) {
        this.className = className;
        this.modifiers = modifiers;
        this.implements = implements;
        this.extend = extend;
        this.implement = implement;
        this.java_field_declarations = new ArrayList<>();
    }

    public java_Class_declaration(
        String className,        String modifiers,        String implements,        String extend,        String implement        ArrayList<java_Field_declaration> java_field_declarations    ) {
        this.className = className;
        this.modifiers = modifiers;
        this.implements = implements;
        this.extend = extend;
        this.implement = implement;
        this.java_field_declarations = java_field_declarations;
    }

    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }
    public String getModifiers() {
        return modifiers;
    }

    public void setModifiers(String modifiers) {
        this.modifiers = modifiers;
    }
    public String getImplements() {
        return implements;
    }

    public void setImplements(String implements) {
        this.implements = implements;
    }
    public String getExtend() {
        return extend;
    }

    public void setExtend(String extend) {
        this.extend = extend;
    }
    public String getImplement() {
        return implement;
    }

    public void setImplement(String implement) {
        this.implement = implement;
    }

    public List<java_Field_declaration> getJava_field_declarations() {
        return java_field_declarations;
    }

    public void addJava_field_declaration(Java_field_declaration java_field_declaration) {
        this.java_field_declarations.add(java_field_declaration);
    }

}