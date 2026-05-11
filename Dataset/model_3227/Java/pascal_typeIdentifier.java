





import java.util.List;
import java.util.ArrayList;

public class pascal_typeIdentifier  {

    private String integer;
    private String boolean;
    private String string;
    private String char;
    private String real;





    private pascal_identifier pascal_identifier;




    private pascal_functionDeclaration pascal_functiondeclaration;




    private pascal_functionType pascal_functiontype;


    public pascal_typeIdentifier(
        String integer,        String boolean,        String string,        String char,        String real    ) {
        this.integer = integer;
        this.boolean = boolean;
        this.string = string;
        this.char = char;
        this.real = real;
    }


    public String getInteger() {
        return integer;
    }

    public void setInteger(String integer) {
        this.integer = integer;
    }
    public String getBoolean() {
        return boolean;
    }

    public void setBoolean(String boolean) {
        this.boolean = boolean;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }
    public String getChar() {
        return char;
    }

    public void setChar(String char) {
        this.char = char;
    }
    public String getReal() {
        return real;
    }

    public void setReal(String real) {
        this.real = real;
    }

    public pascal_identifier getPascal_identifier() {
        return pascal_identifier;
    }

    public void setPascal_identifier(pascal_identifier pascal_identifier) {
        this.pascal_identifier = pascal_identifier;
    }
    public pascal_functionDeclaration getPascal_functiondeclaration() {
        return pascal_functiondeclaration;
    }

    public void setPascal_functiondeclaration(pascal_functionDeclaration pascal_functiondeclaration) {
        this.pascal_functiondeclaration = pascal_functiondeclaration;
    }
    public pascal_functionType getPascal_functiontype() {
        return pascal_functiontype;
    }

    public void setPascal_functiontype(pascal_functionType pascal_functiontype) {
        this.pascal_functiontype = pascal_functiontype;
    }

}