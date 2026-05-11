





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_Attribute  {

    private String type;
    private String attribute;
    private String name;





    private reqLanguage_MainAttributes reqlanguage_mainattributes;


    public reqLanguage_Attribute(
        String type,        String attribute,        String name    ) {
        this.type = type;
        this.attribute = attribute;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public reqLanguage_MainAttributes getReqlanguage_mainattributes() {
        return reqlanguage_mainattributes;
    }

    public void setReqlanguage_mainattributes(reqLanguage_MainAttributes reqlanguage_mainattributes) {
        this.reqlanguage_mainattributes = reqlanguage_mainattributes;
    }

}