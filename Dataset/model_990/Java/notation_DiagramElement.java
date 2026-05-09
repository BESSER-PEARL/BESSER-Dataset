





import java.util.List;
import java.util.ArrayList;

public class notation_DiagramElement extends Identifier {

    private boolean persistent;
    private boolean visible;



    public notation_DiagramElement(
        boolean persistent,        boolean visible    ) {
        super(
        );
        this.persistent = persistent;
        this.visible = visible;
    }


    public boolean getPersistent() {
        return persistent;
    }

    public void setPersistent(boolean persistent) {
        this.persistent = persistent;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }


}