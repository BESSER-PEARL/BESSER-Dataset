





import java.util.List;
import java.util.ArrayList;

public class UML2_TimeTrigger extends Trigger {

    private boolean isRelative;



    public UML2_TimeTrigger(
        boolean isRelative    ) {
        super(
        );
        this.isRelative = isRelative;
    }


    public boolean getIsrelative() {
        return isRelative;
    }

    public void setIsrelative(boolean isRelative) {
        this.isRelative = isRelative;
    }


}