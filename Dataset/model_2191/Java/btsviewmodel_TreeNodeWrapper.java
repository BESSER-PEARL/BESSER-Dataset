





import java.util.List;
import java.util.ArrayList;

public class btsviewmodel_TreeNodeWrapper  {

    private String parentObject;
    private String object;
    private boolean childrenLoaded;
    private String propertyChangeSupport;
    private String label;





    private List<btsviewmodel_TreeNodeWrapper> btsviewmodel_treenodewrappers;




    private btsviewmodel_TreeNodeWrapper btsviewmodel_treenodewrapper;


    public btsviewmodel_TreeNodeWrapper(
        String parentObject,        String object,        boolean childrenLoaded,        String propertyChangeSupport,        String label    ) {
        this.parentObject = parentObject;
        this.object = object;
        this.childrenLoaded = childrenLoaded;
        this.propertyChangeSupport = propertyChangeSupport;
        this.label = label;
        this.btsviewmodel_treenodewrappers = new ArrayList<>();
    }

    public btsviewmodel_TreeNodeWrapper(
        String parentObject,        String object,        boolean childrenLoaded,        String propertyChangeSupport,        String label        ArrayList<btsviewmodel_TreeNodeWrapper> btsviewmodel_treenodewrappers    ) {
        this.parentObject = parentObject;
        this.object = object;
        this.childrenLoaded = childrenLoaded;
        this.propertyChangeSupport = propertyChangeSupport;
        this.label = label;
        this.btsviewmodel_treenodewrappers = btsviewmodel_treenodewrappers;
    }

    public String getParentobject() {
        return parentObject;
    }

    public void setParentobject(String parentObject) {
        this.parentObject = parentObject;
    }
    public String getObject() {
        return object;
    }

    public void setObject(String object) {
        this.object = object;
    }
    public boolean getChildrenloaded() {
        return childrenLoaded;
    }

    public void setChildrenloaded(boolean childrenLoaded) {
        this.childrenLoaded = childrenLoaded;
    }
    public String getPropertychangesupport() {
        return propertyChangeSupport;
    }

    public void setPropertychangesupport(String propertyChangeSupport) {
        this.propertyChangeSupport = propertyChangeSupport;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<btsviewmodel_TreeNodeWrapper> getBtsviewmodel_treenodewrappers() {
        return btsviewmodel_treenodewrappers;
    }

    public void addBtsviewmodel_treenodewrapper(Btsviewmodel_treenodewrapper btsviewmodel_treenodewrapper) {
        this.btsviewmodel_treenodewrappers.add(btsviewmodel_treenodewrapper);
    }
    public btsviewmodel_TreeNodeWrapper getBtsviewmodel_treenodewrapper() {
        return btsviewmodel_treenodewrapper;
    }

    public void setBtsviewmodel_treenodewrapper(btsviewmodel_TreeNodeWrapper btsviewmodel_treenodewrapper) {
        this.btsviewmodel_treenodewrapper = btsviewmodel_treenodewrapper;
    }

}