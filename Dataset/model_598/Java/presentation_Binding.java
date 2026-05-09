





import java.util.List;
import java.util.ArrayList;

public class presentation_Binding  {

    private String path;
    private String xPath;
    private String elementName;
    private String group;
    private String mixed;





    private List<presentation_EObject> presentation_eobjects;




    private List<presentation_EObject> presentation_eobjects;


    public presentation_Binding(
        String path,        String xPath,        String elementName,        String group,        String mixed    ) {
        this.path = path;
        this.xPath = xPath;
        this.elementName = elementName;
        this.group = group;
        this.mixed = mixed;
        this.presentation_eobjects = new ArrayList<>();
        this.presentation_eobjects = new ArrayList<>();
    }

    public presentation_Binding(
        String path,        String xPath,        String elementName,        String group,        String mixed        ArrayList<presentation_EObject> presentation_eobjects,        ArrayList<presentation_EObject> presentation_eobjects    ) {
        this.path = path;
        this.xPath = xPath;
        this.elementName = elementName;
        this.group = group;
        this.mixed = mixed;
        this.presentation_eobjects = presentation_eobjects;
        this.presentation_eobjects = presentation_eobjects;
    }

    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getXpath() {
        return xPath;
    }

    public void setXpath(String xPath) {
        this.xPath = xPath;
    }
    public String getElementname() {
        return elementName;
    }

    public void setElementname(String elementName) {
        this.elementName = elementName;
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
    public List<presentation_EObject> getPresentation_eobjects() {
        return presentation_eobjects;
    }

    public void addPresentation_eobject(Presentation_eobject presentation_eobject) {
        this.presentation_eobjects.add(presentation_eobject);
    }

}