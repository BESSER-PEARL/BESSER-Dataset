





import java.util.List;
import java.util.ArrayList;

public class gastm_MacroDefinition extends PreprocessorElement {

    private String macroName;
    private String body;



    public gastm_MacroDefinition(
        String macroName,        String body    ) {
        super(
        );
        this.macroName = macroName;
        this.body = body;
    }


    public String getMacroname() {
        return macroName;
    }

    public void setMacroname(String macroName) {
        this.macroName = macroName;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }


}