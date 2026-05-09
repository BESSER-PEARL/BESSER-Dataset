





import java.util.List;
import java.util.ArrayList;

public class henshin_TransformationUnit extends NamedElement {

    private boolean activated;





    private henshin_TransformationSystem henshin_transformationsystem;


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

    public henshin_TransformationSystem getHenshin_transformationsystem() {
        return henshin_transformationsystem;
    }

    public void setHenshin_transformationsystem(henshin_TransformationSystem henshin_transformationsystem) {
        this.henshin_transformationsystem = henshin_transformationsystem;
    }

}