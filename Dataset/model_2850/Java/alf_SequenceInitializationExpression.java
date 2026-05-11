





import java.util.List;
import java.util.ArrayList;

public class alf_SequenceInitializationExpression extends InitializationExpression {

    private boolean isNew;



    public alf_SequenceInitializationExpression(
        boolean isNew    ) {
        super(
        );
        this.isNew = isNew;
    }


    public boolean getIsnew() {
        return isNew;
    }

    public void setIsnew(boolean isNew) {
        this.isNew = isNew;
    }


}