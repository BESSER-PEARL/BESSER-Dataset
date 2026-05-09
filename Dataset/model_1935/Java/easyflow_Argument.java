





import java.util.List;
import java.util.ArrayList;

public class easyflow_Argument  {

    private String sep;
    private String name;
    private String arg;



    public easyflow_Argument(
        String sep,        String name,        String arg    ) {
        this.sep = sep;
        this.name = name;
        this.arg = arg;
    }


    public String getSep() {
        return sep;
    }

    public void setSep(String sep) {
        this.sep = sep;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getArg() {
        return arg;
    }

    public void setArg(String arg) {
        this.arg = arg;
    }


}