





import java.util.List;
import java.util.ArrayList;

public class easyflow_CommandArgument  {

    private String sep;
    private String arg;
    private boolean required;
    private boolean named;
    private String name;



    public easyflow_CommandArgument(
        String sep,        String arg,        boolean required,        boolean named,        String name    ) {
        this.sep = sep;
        this.arg = arg;
        this.required = required;
        this.named = named;
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
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public boolean getNamed() {
        return named;
    }

    public void setNamed(boolean named) {
        this.named = named;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}