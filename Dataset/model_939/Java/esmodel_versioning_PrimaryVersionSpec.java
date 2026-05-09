





import java.util.List;
import java.util.ArrayList;

public class esmodel_versioning_PrimaryVersionSpec extends VersionSpec {

    private int identifier;



    public esmodel_versioning_PrimaryVersionSpec(
        int identifier    ) {
        super(
        );
        this.identifier = identifier;
    }


    public int getIdentifier() {
        return identifier;
    }

    public void setIdentifier(int identifier) {
        this.identifier = identifier;
    }


}