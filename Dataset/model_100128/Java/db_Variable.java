





import java.util.List;
import java.util.ArrayList;

public class db_Variable  {

    private String name;
    private String defaultValue;
    private String type;
    private String scope;



    public db_Variable(
        String name,        String defaultValue,        String type,        String scope    ) {
        this.name = name;
        this.defaultValue = defaultValue;
        this.type = type;
        this.scope = scope;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }


}