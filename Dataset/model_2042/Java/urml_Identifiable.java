





import java.util.List;
import java.util.ArrayList;

public class urml_Identifiable  {

    private boolean isInt;
    private String name;
    private boolean isBool;





    private urml_Identifier urml_identifier;


    public urml_Identifiable(
        boolean isInt,        String name,        boolean isBool    ) {
        this.isInt = isInt;
        this.name = name;
        this.isBool = isBool;
    }


    public boolean getIsint() {
        return isInt;
    }

    public void setIsint(boolean isInt) {
        this.isInt = isInt;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsbool() {
        return isBool;
    }

    public void setIsbool(boolean isBool) {
        this.isBool = isBool;
    }

    public urml_Identifier getUrml_identifier() {
        return urml_identifier;
    }

    public void setUrml_identifier(urml_Identifier urml_identifier) {
        this.urml_identifier = urml_identifier;
    }

}