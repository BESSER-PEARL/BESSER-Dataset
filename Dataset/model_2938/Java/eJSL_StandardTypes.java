





import java.util.List;
import java.util.ArrayList;

public class eJSL_StandardTypes extends Type {

    private boolean autoincrement;
    private String type;
    private String default;
    private boolean notnull;



    public eJSL_StandardTypes(
        boolean autoincrement,        String type,        String default,        boolean notnull    ) {
        super(
        );
        this.autoincrement = autoincrement;
        this.type = type;
        this.default = default;
        this.notnull = notnull;
    }


    public boolean getAutoincrement() {
        return autoincrement;
    }

    public void setAutoincrement(boolean autoincrement) {
        this.autoincrement = autoincrement;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public boolean getNotnull() {
        return notnull;
    }

    public void setNotnull(boolean notnull) {
        this.notnull = notnull;
    }


}