





import java.util.List;
import java.util.ArrayList;

public class mm_pictograms_PictogramElement extends GraphicsAlgorithmContainer {

    private boolean active;
    private boolean visible;





    private PictogramLink pictogramlink;


    public mm_pictograms_PictogramElement(
        boolean active,        boolean visible    ) {
        super(
        );
        this.active = active;
        this.visible = visible;
    }


    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }

    public PictogramLink getPictogramlink() {
        return pictogramlink;
    }

    public void setPictogramlink(PictogramLink pictogramlink) {
        this.pictogramlink = pictogramlink;
    }

}