





import java.util.List;
import java.util.ArrayList;

public class ecore_EAnnotation extends EModelElement {

    private String source;





    private List<ecore_EStringToStringMapEntry> ecore_estringtostringmapentrys;


    public ecore_EAnnotation(
        String source    ) {
        super(
        );
        this.source = source;
        this.ecore_estringtostringmapentrys = new ArrayList<>();
    }

    public ecore_EAnnotation(
        String source        ArrayList<ecore_EStringToStringMapEntry> ecore_estringtostringmapentrys    ) {
        this.source = source;
        this.ecore_estringtostringmapentrys = ecore_estringtostringmapentrys;
    }

    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public List<ecore_EStringToStringMapEntry> getEcore_estringtostringmapentrys() {
        return ecore_estringtostringmapentrys;
    }

    public void addEcore_estringtostringmapentry(Ecore_estringtostringmapentry ecore_estringtostringmapentry) {
        this.ecore_estringtostringmapentrys.add(ecore_estringtostringmapentry);
    }

}