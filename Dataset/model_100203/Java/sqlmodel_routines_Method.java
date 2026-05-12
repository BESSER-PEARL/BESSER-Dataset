





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_routines_Method extends Function {

    private boolean constructor;
    private boolean overriding;



    public sqlmodel_routines_Method(
        boolean constructor,        boolean overriding    ) {
        super(
        );
        this.constructor = constructor;
        this.overriding = overriding;
    }


    public boolean getConstructor() {
        return constructor;
    }

    public void setConstructor(boolean constructor) {
        this.constructor = constructor;
    }
    public boolean getOverriding() {
        return overriding;
    }

    public void setOverriding(boolean overriding) {
        this.overriding = overriding;
    }


}