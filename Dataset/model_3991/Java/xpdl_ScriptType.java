





import java.util.List;
import java.util.ArrayList;

public class xpdl_ScriptType  {

    private String type;
    private String version;
    private String grammar;



    public xpdl_ScriptType(
        String type,        String version,        String grammar    ) {
        this.type = type;
        this.version = version;
        this.grammar = grammar;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
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


}