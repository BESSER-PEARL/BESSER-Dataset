





import java.util.List;
import java.util.ArrayList;

public class Java_Parameter  {

    private String defaultValue;
    private String name;



    public Java_Parameter(
        String defaultValue,        String name    ) {
        this.defaultValue = defaultValue;
        this.name = name;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}