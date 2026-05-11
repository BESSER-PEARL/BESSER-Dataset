





import java.util.List;
import java.util.ArrayList;

public class pascal_constant  {

    private String boolLiteral;
    private String string;
    private boolean nil;
    private String name;
    private String opterator;





    private pascal_number pascal_number;


    public pascal_constant(
        String boolLiteral,        String string,        boolean nil,        String name,        String opterator    ) {
        this.boolLiteral = boolLiteral;
        this.string = string;
        this.nil = nil;
        this.name = name;
        this.opterator = opterator;
    }


    public String getBoolliteral() {
        return boolLiteral;
    }

    public void setBoolliteral(String boolLiteral) {
        this.boolLiteral = boolLiteral;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }
    public boolean getNil() {
        return nil;
    }

    public void setNil(boolean nil) {
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

    public pascal_number getPascal_number() {
        return pascal_number;
    }

    public void setPascal_number(pascal_number pascal_number) {
        this.pascal_number = pascal_number;
    }

}