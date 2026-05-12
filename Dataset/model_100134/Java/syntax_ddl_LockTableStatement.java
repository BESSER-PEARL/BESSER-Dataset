





import java.util.List;
import java.util.ArrayList;

public class syntax_ddl_LockTableStatement extends DefinitionStatement {

    private String shareMode;
    private boolean allowRead;



    public syntax_ddl_LockTableStatement(
        String shareMode,        boolean allowRead    ) {
        super(
        );
        this.shareMode = shareMode;
        this.allowRead = allowRead;
    }


    public String getSharemode() {
        return shareMode;
    }

    public void setSharemode(String shareMode) {
        this.shareMode = shareMode;
    }
    public boolean getAllowread() {
        return allowRead;
    }

    public void setAllowread(boolean allowRead) {
        this.allowRead = allowRead;
    }


}