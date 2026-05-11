





import java.util.List;
import java.util.ArrayList;

public class majordomo_BooleanAction extends Action {

    private boolean value;





    private majordomo_BooleanActor majordomo_booleanactor;


    public majordomo_BooleanAction(
        boolean value    ) {
        super(
        );
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }

    public majordomo_BooleanActor getMajordomo_booleanactor() {
        return majordomo_booleanactor;
    }

    public void setMajordomo_booleanactor(majordomo_BooleanActor majordomo_booleanactor) {
        this.majordomo_booleanactor = majordomo_booleanactor;
    }

}