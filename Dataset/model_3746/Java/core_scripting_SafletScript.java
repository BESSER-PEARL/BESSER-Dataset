





import java.util.List;
import java.util.ArrayList;

public class core_scripting_SafletScript  {

    private String name;
    private String scriptText;



    public core_scripting_SafletScript(
        String name,        String scriptText    ) {
        this.name = name;
        this.scriptText = scriptText;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getScripttext() {
        return scriptText;
    }

    public void setScripttext(String scriptText) {
        this.scriptText = scriptText;
    }


}