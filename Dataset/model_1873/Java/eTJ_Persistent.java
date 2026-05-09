





import java.util.List;
import java.util.ArrayList;

public class eTJ_Persistent extends AllocateResourceAttribute {

    private boolean persistent;



    public eTJ_Persistent(
        boolean persistent    ) {
        super(
        );
        this.persistent = persistent;
    }


    public boolean getPersistent() {
        return persistent;
    }

    public void setPersistent(boolean persistent) {
        this.persistent = persistent;
    }


}