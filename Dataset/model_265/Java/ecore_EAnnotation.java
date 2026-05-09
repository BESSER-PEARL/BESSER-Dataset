





import java.util.List;
import java.util.ArrayList;

public class ecore_EAnnotation extends EModelElement {

    private String source;





    private ecore_EModelElement ecore_emodelelement;




    private List<ecore_EObject> ecore_eobjects;




    private ecore_EModelElement ecore_emodelelement;




    private List<ecore_EStringToStringMapEntry> ecore_estringtostringmapentrys;




    private List<ecore_EObject> ecore_eobjects;


    public ecore_EAnnotation(
        String source    ) {
        super(
        );
        this.source = source;
        this.ecore_eobjects = new ArrayList<>();
        this.ecore_estringtostringmapentrys = new ArrayList<>();
        this.ecore_eobjects = new ArrayList<>();
    }

    public ecore_EAnnotation(
        String source        ArrayList<ecore_EObject> ecore_eobjects,        ArrayList<ecore_EStringToStringMapEntry> ecore_estringtostringmapentrys,        ArrayList<ecore_EObject> ecore_eobjects    ) {
        this.source = source;
        this.ecore_eobjects = ecore_eobjects;
        this.ecore_estringtostringmapentrys = ecore_estringtostringmapentrys;
        this.ecore_eobjects = ecore_eobjects;
    }

    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public ecore_EModelElement getEcore_emodelelement() {
        return ecore_emodelelement;
    }

    public void setEcore_emodelelement(ecore_EModelElement ecore_emodelelement) {
        this.ecore_emodelelement = ecore_emodelelement;
    }
    public List<ecore_EObject> getEcore_eobjects() {
        return ecore_eobjects;
    }

    public void addEcore_eobject(Ecore_eobject ecore_eobject) {
        this.ecore_eobjects.add(ecore_eobject);
    }
    public ecore_EModelElement getEcore_emodelelement() {
        return ecore_emodelelement;
    }

    public void setEcore_emodelelement(ecore_EModelElement ecore_emodelelement) {
        this.ecore_emodelelement = ecore_emodelelement;
    }
    public List<ecore_EStringToStringMapEntry> getEcore_estringtostringmapentrys() {
        return ecore_estringtostringmapentrys;
    }

    public void addEcore_estringtostringmapentry(Ecore_estringtostringmapentry ecore_estringtostringmapentry) {
        this.ecore_estringtostringmapentrys.add(ecore_estringtostringmapentry);
    }
    public List<ecore_EObject> getEcore_eobjects() {
        return ecore_eobjects;
    }

    public void addEcore_eobject(Ecore_eobject ecore_eobject) {
        this.ecore_eobjects.add(ecore_eobject);
    }

}