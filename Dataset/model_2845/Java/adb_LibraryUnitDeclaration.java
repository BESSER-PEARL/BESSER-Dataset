





import java.util.List;
import java.util.ArrayList;

public class adb_LibraryUnitDeclaration extends Unit {

    private boolean private;





    private adb_WithClause adb_withclause;


    public adb_LibraryUnitDeclaration(
        boolean private    ) {
        super(
        );
        this.private = private;
    }


    public boolean getPrivate() {
        return private;
    }

    public void setPrivate(boolean private) {
        this.private = private;
    }

    public adb_WithClause getAdb_withclause() {
        return adb_withclause;
    }

    public void setAdb_withclause(adb_WithClause adb_withclause) {
        this.adb_withclause = adb_withclause;
    }

}