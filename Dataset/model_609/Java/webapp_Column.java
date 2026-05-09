





import java.util.List;
import java.util.ArrayList;

public class webapp_Column  {

    private boolean isNotNull;
    private String type;
    private String name;
    private int size;
    private String defaultValue;
    private boolean useZeroFill;





    private webapp_Table webapp_table;


    public webapp_Column(
        boolean isNotNull,        String type,        String name,        int size,        String defaultValue,        boolean useZeroFill    ) {
        this.isNotNull = isNotNull;
        this.type = type;
        this.name = name;
        this.size = size;
        this.defaultValue = defaultValue;
        this.useZeroFill = useZeroFill;
    }


    public boolean getIsnotnull() {
        return isNotNull;
    }

    public void setIsnotnull(boolean isNotNull) {
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
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public boolean getUsezerofill() {
        return useZeroFill;
    }

    public void setUsezerofill(boolean useZeroFill) {
        this.useZeroFill = useZeroFill;
    }

    public webapp_Table getWebapp_table() {
        return webapp_table;
    }

    public void setWebapp_table(webapp_Table webapp_table) {
        this.webapp_table = webapp_table;
    }

}