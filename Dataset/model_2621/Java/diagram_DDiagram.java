





import java.util.List;
import java.util.ArrayList;

public class diagram_DDiagram extends DRepresentation, DragAndDropTarget {

    private boolean synchronized;
    private boolean isInLayoutingMode;
    private int headerHeight;
    private boolean isInShowingMode;





    private List<AdditionalLayer> additionallayers;




    private List<validation_ValidationRule> validation_validationrules;


    public diagram_DDiagram(
        boolean synchronized,        boolean isInLayoutingMode,        int headerHeight,        boolean isInShowingMode    ) {
        super(
        );
        this.synchronized = synchronized;
        this.isInLayoutingMode = isInLayoutingMode;
        this.headerHeight = headerHeight;
        this.isInShowingMode = isInShowingMode;
        this.additionallayers = new ArrayList<>();
        this.validation_validationrules = new ArrayList<>();
    }

    public diagram_DDiagram(
        boolean synchronized,        boolean isInLayoutingMode,        int headerHeight,        boolean isInShowingMode        ArrayList<AdditionalLayer> additionallayers,        ArrayList<validation_ValidationRule> validation_validationrules    ) {
        this.synchronized = synchronized;
        this.isInLayoutingMode = isInLayoutingMode;
        this.headerHeight = headerHeight;
        this.isInShowingMode = isInShowingMode;
        this.additionallayers = additionallayers;
        this.validation_validationrules = validation_validationrules;
    }

    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }
    public boolean getIsinlayoutingmode() {
        return isInLayoutingMode;
    }

    public void setIsinlayoutingmode(boolean isInLayoutingMode) {
        this.isInLayoutingMode = isInLayoutingMode;
    }
    public int getHeaderheight() {
        return headerHeight;
    }

    public void setHeaderheight(int headerHeight) {
        this.headerHeight = headerHeight;
    }
    public boolean getIsinshowingmode() {
        return isInShowingMode;
    }

    public void setIsinshowingmode(boolean isInShowingMode) {
        this.isInShowingMode = isInShowingMode;
    }

    public List<AdditionalLayer> getAdditionallayers() {
        return additionallayers;
    }

    public void addAdditionallayer(Additionallayer additionallayer) {
        this.additionallayers.add(additionallayer);
    }
    public List<validation_ValidationRule> getValidation_validationrules() {
        return validation_validationrules;
    }

    public void addValidation_validationrule(Validation_validationrule validation_validationrule) {
        this.validation_validationrules.add(validation_validationrule);
    }

}