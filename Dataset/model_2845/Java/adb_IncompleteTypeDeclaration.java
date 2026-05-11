





import java.util.List;
import java.util.ArrayList;

public class adb_IncompleteTypeDeclaration extends NewTypeDeclaration {

    private boolean tagged;



    public adb_IncompleteTypeDeclaration(
        boolean tagged    ) {
        super(
        );
        this.tagged = tagged;
    }


    public boolean getTagged() {
        return tagged;
    }

    public void setTagged(boolean tagged) {
        this.tagged = tagged;
    }


}