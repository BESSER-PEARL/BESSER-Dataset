





import java.util.List;
import java.util.ArrayList;

public class presentation_CellEditor  {

    private String mixed;
    private String group;
    private String style;
    private String errorMessage;





    private List<presentation_EObject> presentation_eobjects;




    private presentation_ColumnViewer presentation_columnviewer;




    private List<presentation_Control> presentation_controls;


    public presentation_CellEditor(
        String mixed,        String group,        String style,        String errorMessage    ) {
        this.mixed = mixed;
        this.group = group;
        this.style = style;
        this.errorMessage = errorMessage;
        this.presentation_eobjects = new ArrayList<>();
        this.presentation_controls = new ArrayList<>();
    }

    public presentation_CellEditor(
        String mixed,        String group,        String style,        String errorMessage        ArrayList<presentation_EObject> presentation_eobjects,        ArrayList<presentation_Control> presentation_controls    ) {
        this.mixed = mixed;
        this.group = group;
        this.style = style;
        this.errorMessage = errorMessage;
        this.presentation_eobjects = presentation_eobjects;
        this.presentation_controls = presentation_controls;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getErrormessage() {
        return errorMessage;
    }

    public void setErrormessage(String errorMessage) {
        this.errorMessage = errorMessage;
    }

    public List<presentation_EObject> getPresentation_eobjects() {
        return presentation_eobjects;
    }

    public void addPresentation_eobject(Presentation_eobject presentation_eobject) {
        this.presentation_eobjects.add(presentation_eobject);
    }
    public presentation_ColumnViewer getPresentation_columnviewer() {
        return presentation_columnviewer;
    }

    public void setPresentation_columnviewer(presentation_ColumnViewer presentation_columnviewer) {
        this.presentation_columnviewer = presentation_columnviewer;
    }
    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }

}