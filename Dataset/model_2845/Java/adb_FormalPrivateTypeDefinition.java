





import java.util.List;
import java.util.ArrayList;

public class adb_FormalPrivateTypeDefinition extends FormalTypeDefinition {

    private boolean limited;
    private boolean abstract;
    private boolean tagged;



    public adb_FormalPrivateTypeDefinition(
        boolean limited,        boolean abstract,        boolean tagged    ) {
        super(
        );
        this.limited = limited;
        this.abstract = abstract;
        this.tagged = tagged;
    }


    public boolean getLimited() {
        return limited;
    }

    public void setLimited(boolean limited) {
        this.limited = limited;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getTagged() {
        return tagged;
    }

    public void setTagged(boolean tagged) {
        this.tagged = tagged;
    }


}