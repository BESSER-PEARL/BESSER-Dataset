





import java.util.List;
import java.util.ArrayList;

public class astm_gastm_MacroDefinition extends PreprocessorElement {

    private String body;
    private String macroName;



    public astm_gastm_MacroDefinition(
        String body,        String macroName    ) {
        super(
        );
        this.body = body;
        this.macroName = macroName;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getMacroname() {
        return macroName;
    }

    public void setMacroname(String macroName) {
        this.macroName = macroName;
    }


}