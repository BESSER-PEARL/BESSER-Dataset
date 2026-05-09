





import java.util.List;
import java.util.ArrayList;

public class easyflow_Interpreter  {

    private String options;
    private String name;
    private String exe;
    private String subCmd;



    public easyflow_Interpreter(
        String options,        String name,        String exe,        String subCmd    ) {
        this.options = options;
        this.name = name;
        this.exe = exe;
        this.subCmd = subCmd;
    }


    public String getOptions() {
        return options;
    }

    public void setOptions(String options) {
        this.options = options;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getExe() {
        return exe;
    }

    public void setExe(String exe) {
        this.exe = exe;
    }
    public String getSubcmd() {
        return subCmd;
    }

    public void setSubcmd(String subCmd) {
        this.subCmd = subCmd;
    }


}