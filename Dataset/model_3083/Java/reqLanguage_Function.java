





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_Function  {

    private String function;
    private String type;
    private String name;





    private reqLanguage_MainFunctions reqlanguage_mainfunctions;


    public reqLanguage_Function(
        String function,        String type,        String name    ) {
        this.function = function;
        this.type = type;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public reqLanguage_MainFunctions getReqlanguage_mainfunctions() {
        return reqlanguage_mainfunctions;
    }

    public void setReqlanguage_mainfunctions(reqLanguage_MainFunctions reqlanguage_mainfunctions) {
        this.reqlanguage_mainfunctions = reqlanguage_mainfunctions;
    }

}