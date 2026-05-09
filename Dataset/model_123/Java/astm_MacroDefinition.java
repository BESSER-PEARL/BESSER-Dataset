





import java.util.List;
import java.util.ArrayList;

public class astm_MacroDefinition extends PreprocessorElement {

    private String body;
    private String macroName;





    private astm_MacroCall astm_macrocall;


    public astm_MacroDefinition(
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

    public astm_MacroCall getAstm_macrocall() {
        return astm_macrocall;
    }

    public void setAstm_macrocall(astm_MacroCall astm_macrocall) {
        this.astm_macrocall = astm_macrocall;
    }

}