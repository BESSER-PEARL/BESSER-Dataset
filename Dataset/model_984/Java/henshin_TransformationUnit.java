





import java.util.List;
import java.util.ArrayList;

public class henshin_TransformationUnit extends NamedElement {

    private boolean activated;



    public henshin_TransformationUnit(
        boolean activated    ) {
        super(
        );
        this.activated = activated;
    }


    public boolean getActivated() {
        return activated;
    }

    public void setActivated(boolean activated) {
        this.activated = activated;
    }


}