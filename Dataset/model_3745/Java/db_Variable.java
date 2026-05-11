





import java.util.List;
import java.util.ArrayList;

public class db_Variable  {

    private String type;
    private String scope;
    private String name;
    private String defaultValue;



    public db_Variable(
        String type,        String scope,        String name,        String defaultValue    ) {
        this.type = type;
        this.scope = scope;
        this.name = name;
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


}