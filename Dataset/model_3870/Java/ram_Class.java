





import java.util.List;
import java.util.ArrayList;

public class ram_Class extends Classifier {

    private boolean abstract;
    private boolean partial;



    public ram_Class(
        boolean abstract,        boolean partial    ) {
        super(
        );
        this.abstract = abstract;
        this.partial = partial;
    }


    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getPartial() {
        return partial;
    }

    public void setPartial(boolean partial) {
        this.partial = partial;
    }


}