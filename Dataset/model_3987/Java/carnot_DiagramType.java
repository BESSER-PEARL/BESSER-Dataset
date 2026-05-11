





import java.util.List;
import java.util.ArrayList;

public class carnot_DiagramType extends IExtensibleElement, ISymbolContainer, IModelElement {

    private String mode;
    private String orientation;
    private String name;



    public carnot_DiagramType(
        String mode,        String orientation,        String name    ) {
        super(
        );
        this.mode = mode;
        this.orientation = orientation;
        this.name = name;
    }


    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }
    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}