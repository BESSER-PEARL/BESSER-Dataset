





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EAnnotation extends EModelElement {

    private String source;





    private List<ecoreDiff_EStringToStringMapEntry> ecorediff_estringtostringmapentrys;




    private ecoreDiff_EModelElement ecorediff_emodelelement;




    private List<ecoreDiff_EObject> ecorediff_eobjects;




    private List<ecoreDiff_EObject> ecorediff_eobjects;




    private ecoreDiff_EModelElement ecorediff_emodelelement;


    public ecoreDiff_EAnnotation(
        String source    ) {
        super(
        );
        this.source = source;
        this.ecorediff_estringtostringmapentrys = new ArrayList<>();
        this.ecorediff_eobjects = new ArrayList<>();
        this.ecorediff_eobjects = new ArrayList<>();
    }

    public ecoreDiff_EAnnotation(
        String source        ArrayList<ecoreDiff_EStringToStringMapEntry> ecorediff_estringtostringmapentrys,        ArrayList<ecoreDiff_EObject> ecorediff_eobjects,        ArrayList<ecoreDiff_EObject> ecorediff_eobjects    ) {
        this.source = source;
        this.ecorediff_estringtostringmapentrys = ecorediff_estringtostringmapentrys;
        this.ecorediff_eobjects = ecorediff_eobjects;
        this.ecorediff_eobjects = ecorediff_eobjects;
    }

    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public List<ecoreDiff_EStringToStringMapEntry> getEcorediff_estringtostringmapentrys() {
        return ecorediff_estringtostringmapentrys;
    }

    public void addEcorediff_estringtostringmapentry(Ecorediff_estringtostringmapentry ecorediff_estringtostringmapentry) {
        this.ecorediff_estringtostringmapentrys.add(ecorediff_estringtostringmapentry);
    }
    public ecoreDiff_EModelElement getEcorediff_emodelelement() {
        return ecorediff_emodelelement;
    }

    public void setEcorediff_emodelelement(ecoreDiff_EModelElement ecorediff_emodelelement) {
        this.ecorediff_emodelelement = ecorediff_emodelelement;
    }
    public List<ecoreDiff_EObject> getEcorediff_eobjects() {
        return ecorediff_eobjects;
    }

    public void addEcorediff_eobject(Ecorediff_eobject ecorediff_eobject) {
        this.ecorediff_eobjects.add(ecorediff_eobject);
    }
    public List<ecoreDiff_EObject> getEcorediff_eobjects() {
        return ecorediff_eobjects;
    }

    public void addEcorediff_eobject(Ecorediff_eobject ecorediff_eobject) {
        this.ecorediff_eobjects.add(ecorediff_eobject);
    }
    public ecoreDiff_EModelElement getEcorediff_emodelelement() {
        return ecorediff_emodelelement;
    }

    public void setEcorediff_emodelelement(ecoreDiff_EModelElement ecorediff_emodelelement) {
        this.ecorediff_emodelelement = ecorediff_emodelelement;
    }

}