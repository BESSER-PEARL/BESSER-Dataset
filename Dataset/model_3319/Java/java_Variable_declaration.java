





import java.util.List;
import java.util.ArrayList;

public class java_Variable_declaration  {

    private String modifiers;





    private List<java_Variable_declarator> java_variable_declarators;




    private java_Variable_declarator java_variable_declarator;




    private java_Type java_type;


    public java_Variable_declaration(
        String modifiers    ) {
        this.modifiers = modifiers;
        this.java_variable_declarators = new ArrayList<>();
    }

    public java_Variable_declaration(
        String modifiers        ArrayList<java_Variable_declarator> java_variable_declarators    ) {
        this.modifiers = modifiers;
        this.java_variable_declarators = java_variable_declarators;
    }

    public String getModifiers() {
        return modifiers;
    }

    public void setModifiers(String modifiers) {
        this.modifiers = modifiers;
    }

    public List<java_Variable_declarator> getJava_variable_declarators() {
        return java_variable_declarators;
    }

    public void addJava_variable_declarator(Java_variable_declarator java_variable_declarator) {
        this.java_variable_declarators.add(java_variable_declarator);
    }
    public java_Variable_declarator getJava_variable_declarator() {
        return java_variable_declarator;
    }

    public void setJava_variable_declarator(java_Variable_declarator java_variable_declarator) {
        this.java_variable_declarator = java_variable_declarator;
    }
    public java_Type getJava_type() {
        return java_type;
    }

    public void setJava_type(java_Type java_type) {
        this.java_type = java_type;
    }

}