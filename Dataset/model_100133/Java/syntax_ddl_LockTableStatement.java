





import java.util.List;
import java.util.ArrayList;

public class syntax_ddl_LockTableStatement extends DefinitionStatement {

    private boolean allowRead;
    private String shareMode;



    public syntax_ddl_LockTableStatement(
        boolean allowRead,        String shareMode    ) {
        super(
        );
        this.allowRead = allowRead;
        this.shareMode = shareMode;
    }


    public boolean getAllowread() {
        return allowRead;
    }

    public void setAllowread(boolean allowRead) {
        this.allowRead = allowRead;
    }
    public String getSharemode() {
        return shareMode;
    }

    public void setSharemode(String shareMode) {
        this.shareMode = shareMode;
    }


}