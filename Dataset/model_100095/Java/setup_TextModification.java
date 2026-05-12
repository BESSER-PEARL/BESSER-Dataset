





import java.util.List;
import java.util.ArrayList;

public class setup_TextModification  {

    private String substitutions;
    private String pattern;





    private setup_TextModifyTask setup_textmodifytask;


    public setup_TextModification(
        String substitutions,        String pattern    ) {
        this.substitutions = substitutions;
        this.pattern = pattern;
    }


    public String getSubstitutions() {
        return substitutions;
    }

    public void setSubstitutions(String substitutions) {
        this.substitutions = substitutions;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }

    public setup_TextModifyTask getSetup_textmodifytask() {
        return setup_textmodifytask;
    }

    public void setSetup_textmodifytask(setup_TextModifyTask setup_textmodifytask) {
        this.setup_textmodifytask = setup_textmodifytask;
    }

}