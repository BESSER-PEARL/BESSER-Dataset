





import java.util.List;
import java.util.ArrayList;

public class adb_RecordTypeDefinition extends TypeDefinition {

    private boolean abstract;
    private boolean tagged;
    private boolean limited;



    public adb_RecordTypeDefinition(
        boolean abstract,        boolean tagged,        boolean limited    ) {
        super(
        );
        this.abstract = abstract;
        this.tagged = tagged;
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
    public boolean getLimited() {
        return limited;
    }

    public void setLimited(boolean limited) {
        this.limited = limited;
    }


}