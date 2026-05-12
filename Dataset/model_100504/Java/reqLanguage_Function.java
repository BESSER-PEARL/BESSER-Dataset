





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_Function  {

    private String name;
    private String function;
    private String type;





    private reqLanguage_MainFunctions reqlanguage_mainfunctions;


    public reqLanguage_Function(
        String name,        String function,        String type    ) {
        this.name = name;
        this.function = function;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public reqLanguage_MainFunctions getReqlanguage_mainfunctions() {
        return reqlanguage_mainfunctions;
    }

    public void setReqlanguage_mainfunctions(reqLanguage_MainFunctions reqlanguage_mainfunctions) {
        this.reqlanguage_mainfunctions = reqlanguage_mainfunctions;
    }

}