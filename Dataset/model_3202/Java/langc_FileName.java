





import java.util.List;
import java.util.ArrayList;

public class langc_FileName extends Name {

    private boolean hasObjectCode;





    private langc_FileDependency langc_filedependency;


    public langc_FileName(
        boolean hasObjectCode    ) {
        super(
        );
        this.hasObjectCode = hasObjectCode;
    }


    public boolean getHasobjectcode() {
        return hasObjectCode;
    }

    public void setHasobjectcode(boolean hasObjectCode) {
        this.hasObjectCode = hasObjectCode;
    }

    public langc_FileDependency getLangc_filedependency() {
        return langc_filedependency;
    }

    public void setLangc_filedependency(langc_FileDependency langc_filedependency) {
        this.langc_filedependency = langc_filedependency;
    }

}