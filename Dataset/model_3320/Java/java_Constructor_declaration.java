





import java.util.List;
import java.util.ArrayList;

public class java_Constructor_declaration  {

    private String modifiers;
    private String name;





    private java_Statement_block java_statement_block;


    public java_Constructor_declaration(
        String modifiers,        String name    ) {
        this.modifiers = modifiers;
        this.name = name;
    }


    public String getModifiers() {
        return modifiers;
    }

    public void setModifiers(String modifiers) {
        this.modifiers = modifiers;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public java_Statement_block getJava_statement_block() {
        return java_statement_block;
    }

    public void setJava_statement_block(java_Statement_block java_statement_block) {
        this.java_statement_block = java_statement_block;
    }

}