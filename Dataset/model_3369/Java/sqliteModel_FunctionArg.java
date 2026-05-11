





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_FunctionArg  {

    private String type;
    private String name;



    public sqliteModel_FunctionArg(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
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


}