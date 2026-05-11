





import java.util.List;
import java.util.ArrayList;

public class grammarSql_Column  {

    private String type;
    private String name;
    private boolean isNotNull;



    public grammarSql_Column(
        String type,        String name,        boolean isNotNull    ) {
        this.type = type;
        this.name = name;
        this.isNotNull = isNotNull;
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
    public boolean getIsnotnull() {
        return isNotNull;
    }

    public void setIsnotnull(boolean isNotNull) {
        this.isNotNull = isNotNull;
    }


}