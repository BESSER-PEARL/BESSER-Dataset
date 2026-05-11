





import java.util.List;
import java.util.ArrayList;

public class types_Type extends Declaration {

    private boolean abstract;
    private boolean visible;



    public types_Type(
        boolean abstract,        boolean visible    ) {
        super(
        );
        this.abstract = abstract;
        this.visible = visible;
    }


    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }


}