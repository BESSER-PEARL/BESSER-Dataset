





import java.util.List;
import java.util.ArrayList;

public class xpdl2_ScriptType  {

    private String version;
    private String grammar;
    private String type;



    public xpdl2_ScriptType(
        String version,        String grammar,        String type    ) {
        this.version = version;
        this.grammar = grammar;
        this.type = type;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getGrammar() {
        return grammar;
    }

    public void setGrammar(String grammar) {
        this.grammar = grammar;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}