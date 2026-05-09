





import java.util.List;
import java.util.ArrayList;

public class easyflow_Argument  {

    private String name;
    private String sep;
    private String arg;



    public easyflow_Argument(
        String name,        String sep,        String arg    ) {
        this.name = name;
        this.sep = sep;
        this.arg = arg;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSep() {
        return sep;
    }

    public void setSep(String sep) {
        this.sep = sep;
    }
    public String getArg() {
        return arg;
    }

    public void setArg(String arg) {
        this.arg = arg;
    }


}