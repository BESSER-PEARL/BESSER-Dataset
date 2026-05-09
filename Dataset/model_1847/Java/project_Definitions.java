





import java.util.List;
import java.util.ArrayList;

public class project_Definitions extends ExportAttribute {

    private boolean all;
    private boolean none;



    public project_Definitions(
        boolean all,        boolean none    ) {
        super(
        );
        this.all = all;
        this.none = none;
    }


    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }
    public boolean getNone() {
        return none;
    }

    public void setNone(boolean none) {
        this.none = none;
    }


}