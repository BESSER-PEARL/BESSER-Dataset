





import java.util.List;
import java.util.ArrayList;

public class presentation_Binding  {

    private String mixed;
    private String path;
    private String group;
    private String elementName;
    private String xPath;





    private List<presentation_EObject> presentation_eobjects;




    private List<presentation_Widget> presentation_widgets;




    private List<presentation_EObject> presentation_eobjects;


    public presentation_Binding(
        String mixed,        String path,        String group,        String elementName,        String xPath    ) {
        this.mixed = mixed;
        this.path = path;
        this.group = group;
        this.elementName = elementName;
        this.xPath = xPath;
        this.presentation_eobjects = new ArrayList<>();
        this.presentation_widgets = new ArrayList<>();
        this.presentation_eobjects = new ArrayList<>();
    }

    public presentation_Binding(
        String mixed,        String path,        String group,        String elementName,        String xPath        ArrayList<presentation_EObject> presentation_eobjects,        ArrayList<presentation_Widget> presentation_widgets,        ArrayList<presentation_EObject> presentation_eobjects    ) {
        this.mixed = mixed;
        this.path = path;
        this.group = group;
        this.elementName = elementName;
        this.xPath = xPath;
        this.presentation_eobjects = presentation_eobjects;
        this.presentation_widgets = presentation_widgets;
        this.presentation_eobjects = presentation_eobjects;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getElementname() {
        return elementName;
    }

    public void setElementname(String elementName) {
        this.elementName = elementName;
    }
    public String getXpath() {
        return xPath;
    }

    public void setXpath(String xPath) {
        this.xPath = xPath;
    }

    public List<presentation_EObject> getPresentation_eobjects() {
        return presentation_eobjects;
    }

    public void addPresentation_eobject(Presentation_eobject presentation_eobject) {
        this.presentation_eobjects.add(presentation_eobject);
    }
    public List<presentation_Widget> getPresentation_widgets() {
        return presentation_widgets;
    }

    public void addPresentation_widget(Presentation_widget presentation_widget) {
        this.presentation_widgets.add(presentation_widget);
    }
    public List<presentation_EObject> getPresentation_eobjects() {
        return presentation_eobjects;
    }

    public void addPresentation_eobject(Presentation_eobject presentation_eobject) {
        this.presentation_eobjects.add(presentation_eobject);
    }

}