





import java.util.List;
import java.util.ArrayList;

public class adb_WithClause extends ContextItem {

    private boolean private;
    private boolean limited;



    public adb_WithClause(
        boolean private,        boolean limited    ) {
        super(
        );
        this.private = private;
        this.limited = limited;
    }


    public boolean getPrivate() {
        return private;
    }

    public void setPrivate(boolean private) {
        this.private = private;
    }
    public boolean getLimited() {
        return limited;
    }

    public void setLimited(boolean limited) {
        this.limited = limited;
    }


}