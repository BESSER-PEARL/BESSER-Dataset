





import java.util.List;
import java.util.ArrayList;

public class presentation_CellEditor  {

    private String errorMessage;
    private String style;
    private String group;
    private String mixed;





    private List<presentation_EObject> presentation_eobjects;




    private List<presentation_Control> presentation_controls;




    private presentation_ColumnViewer presentation_columnviewer;


    public presentation_CellEditor(
        String errorMessage,        String style,        String group,        String mixed    ) {
        this.errorMessage = errorMessage;
        this.style = style;
        this.group = group;
        this.mixed = mixed;
        this.presentation_eobjects = new ArrayList<>();
        this.presentation_controls = new ArrayList<>();
    }

    public presentation_CellEditor(
        String errorMessage,        String style,        String group,        String mixed        ArrayList<presentation_EObject> presentation_eobjects,        ArrayList<presentation_Control> presentation_controls    ) {
        this.errorMessage = errorMessage;
        this.style = style;
        this.group = group;
        this.mixed = mixed;
        this.presentation_eobjects = presentation_eobjects;
        this.presentation_controls = presentation_controls;
    }

    public String getErrormessage() {
        return errorMessage;
    }

    public void setErrormessage(String errorMessage) {
        this.errorMessage = errorMessage;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<presentation_EObject> getPresentation_eobjects() {
        return presentation_eobjects;
    }

    public void addPresentation_eobject(Presentation_eobject presentation_eobject) {
        this.presentation_eobjects.add(presentation_eobject);
    }
    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }
    public presentation_ColumnViewer getPresentation_columnviewer() {
        return presentation_columnviewer;
    }

    public void setPresentation_columnviewer(presentation_ColumnViewer presentation_columnviewer) {
        this.presentation_columnviewer = presentation_columnviewer;
    }

}