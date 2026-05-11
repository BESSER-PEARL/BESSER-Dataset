





import java.util.List;
import java.util.ArrayList;

public class langc_SwitchClause extends CodeBlock {

    private boolean fallthrough;





    private langc_SwitchStatement langc_switchstatement;


    public langc_SwitchClause(
        boolean fallthrough    ) {
        super(
        );
        this.fallthrough = fallthrough;
    }


    public boolean getFallthrough() {
        return fallthrough;
    }

    public void setFallthrough(boolean fallthrough) {
        this.fallthrough = fallthrough;
    }

    public langc_SwitchStatement getLangc_switchstatement() {
        return langc_switchstatement;
    }

    public void setLangc_switchstatement(langc_SwitchStatement langc_switchstatement) {
        this.langc_switchstatement = langc_switchstatement;
    }

}