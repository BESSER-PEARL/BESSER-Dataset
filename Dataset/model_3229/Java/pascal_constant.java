





import java.util.List;
import java.util.ArrayList;

public class pascal_constant  {

    private String boolLiteral;
    private String name;
    private String opterator;
    private String nil;
    private String string;





    private pascal_number pascal_number;


    public pascal_constant(
        String boolLiteral,        String name,        String opterator,        String nil,        String string    ) {
        this.boolLiteral = boolLiteral;
        this.name = name;
        this.opterator = opterator;
        this.nil = nil;
        this.string = string;
    }


    public String getBoolliteral() {
        return boolLiteral;
    }

    public void setBoolliteral(String boolLiteral) {
        this.boolLiteral = boolLiteral;
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
    public String getNil() {
        return nil;
    }

    public void setNil(String nil) {
        this.nil = nil;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }

    public pascal_number getPascal_number() {
        return pascal_number;
    }

    public void setPascal_number(pascal_number pascal_number) {
        this.pascal_number = pascal_number;
    }

}