





import java.util.List;
import java.util.ArrayList;

public class diagram_description_ContainerMapping extends description_AbstractNodeMapping, description_DragAndDropTargetDescription {

    private String childrenPresentation;



    public diagram_description_ContainerMapping(
        String childrenPresentation    ) {
        super(
        );
        this.childrenPresentation = childrenPresentation;
    }


    public String getChildrenpresentation() {
        return childrenPresentation;
    }

    public void setChildrenpresentation(String childrenPresentation) {
        this.childrenPresentation = childrenPresentation;
    }


}