





import java.util.List;
import java.util.ArrayList;

public class carnot_DiagramType extends ISymbolContainer, IExtensibleElement, IModelElement {

    private String orientation;
    private String mode;
    private String name;



    public carnot_DiagramType(
        String orientation,        String mode,        String name    ) {
        super(
        );
        this.orientation = orientation;
        this.mode = mode;
        this.name = name;
    }


    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}