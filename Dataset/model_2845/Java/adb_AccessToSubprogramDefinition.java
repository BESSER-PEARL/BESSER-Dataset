





import java.util.List;
import java.util.ArrayList;

public class adb_AccessToSubprogramDefinition extends AccessSpecification, NotNullAccessDefinition {

    private boolean protected;



    public adb_AccessToSubprogramDefinition(
        boolean protected    ) {
        super(
        );
        this.protected = protected;
    }


    public boolean getProtected() {
        return protected;
    }

    public void setProtected(boolean protected) {
        this.protected = protected;
    }


}