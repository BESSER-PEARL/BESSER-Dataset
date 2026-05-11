





import java.util.List;
import java.util.ArrayList;

public class dmx_DmxContextReference extends DExpression {

    private boolean before;
    private boolean all;



    public dmx_DmxContextReference(
        boolean before,        boolean all    ) {
        super(
        );
        this.before = before;
        this.all = all;
    }


    public boolean getBefore() {
        return before;
    }

    public void setBefore(boolean before) {
        this.before = before;
    }
    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }


}