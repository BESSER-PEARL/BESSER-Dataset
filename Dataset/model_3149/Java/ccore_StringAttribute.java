





import java.util.List;
import java.util.ArrayList;

public class ccore_StringAttribute extends Attribute {

    private boolean notEmpty;



    public ccore_StringAttribute(
        boolean notEmpty    ) {
        super(
        );
        this.notEmpty = notEmpty;
    }


    public boolean getNotempty() {
        return notEmpty;
    }

    public void setNotempty(boolean notEmpty) {
        this.notEmpty = notEmpty;
    }


}