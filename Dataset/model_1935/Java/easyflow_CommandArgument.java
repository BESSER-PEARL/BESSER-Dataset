





import java.util.List;
import java.util.ArrayList;

public class easyflow_CommandArgument  {

    private String arg;
    private boolean required;
    private String sep;
    private String name;
    private boolean named;



    public easyflow_CommandArgument(
        String arg,        boolean required,        String sep,        String name,        boolean named    ) {
        this.arg = arg;
        this.required = required;
        this.sep = sep;
        this.name = name;
        this.named = named;
    }


    public String getArg() {
        return arg;
    }

    public void setArg(String arg) {
        this.arg = arg;
    }
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
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
    public boolean getNamed() {
        return named;
    }

    public void setNamed(boolean named) {
        this.named = named;
    }


}