





import java.util.List;
import java.util.ArrayList;

public class pascal_constant  {

    private String name;
    private String opterator;
    private String string;
    private String boolLiteral;
    private String nil;





    private pascal_constant_definition pascal_constant_definition;


    public pascal_constant(
        String name,        String opterator,        String string,        String boolLiteral,        String nil    ) {
        this.name = name;
        this.opterator = opterator;
        this.string = string;
        this.boolLiteral = boolLiteral;
        this.nil = nil;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOpterator() {
        return opterator;
    }

    public void setOpterator(String opterator) {
        this.opterator = opterator;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }
    public String getBoolliteral() {
        return boolLiteral;
    }

    public void setBoolliteral(String boolLiteral) {
        this.boolLiteral = boolLiteral;
    }
    public String getNil() {
        return nil;
    }

    public void setNil(String nil) {
        this.nil = nil;
    }

    public pascal_constant_definition getPascal_constant_definition() {
        return pascal_constant_definition;
    }

    public void setPascal_constant_definition(pascal_constant_definition pascal_constant_definition) {
        this.pascal_constant_definition = pascal_constant_definition;
    }

}