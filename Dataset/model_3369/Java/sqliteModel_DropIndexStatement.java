





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_DropIndexStatement extends DDLStatement {

    private boolean ifExists;



    public sqliteModel_DropIndexStatement(
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