





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_DropTriggerStatement extends DDLStatement {

    private boolean ifExists;



    public sqliteModel_DropTriggerStatement(
        boolean ifExists    ) {
        super(
        );
        this.ifExists = ifExists;
    }


    public boolean getIfexists() {
        return ifExists;
    }

    public void setIfexists(boolean ifExists) {
        this.ifExists = ifExists;
    }


}