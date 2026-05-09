





import java.util.List;
import java.util.ArrayList;

public class eTJ_Definitions extends ExportAttribute {

    private boolean none;
    private boolean all;



    public eTJ_Definitions(
        boolean none,        boolean all    ) {
        super(
        );
        this.none = none;
        this.all = all;
    }


    public boolean getNone() {
        return none;
    }

    public void setNone(boolean none) {
        this.none = none;
    }
    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }


}