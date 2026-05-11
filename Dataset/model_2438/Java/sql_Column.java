





import java.util.List;
import java.util.ArrayList;

public class sql_Column  {

    private String type;
    private boolean isNotNull;
    private String name;



    public sql_Column(
        String type,        boolean isNotNull,        String name    ) {
        this.type = type;
        this.isNotNull = isNotNull;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getIsnotnull() {
        return isNotNull;
    }

    public void setIsnotnull(boolean isNotNull) {
        this.isNotNull = isNotNull;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}