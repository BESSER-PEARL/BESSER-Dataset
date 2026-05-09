





import java.util.List;
import java.util.ArrayList;

public class presentation_DocumentRoot  {

    private String mixed;





    private List<presentation_Composite> presentation_composites;




    private List<presentation_EStringToStringMapEntry> presentation_estringtostringmapentrys;




    private List<presentation_EStringToStringMapEntry> presentation_estringtostringmapentrys;


    public presentation_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.presentation_composites = new ArrayList<>();
        this.presentation_estringtostringmapentrys = new ArrayList<>();
        this.presentation_estringtostringmapentrys = new ArrayList<>();
    }

    public presentation_DocumentRoot(
        String mixed        ArrayList<presentation_Composite> presentation_composites,        ArrayList<presentation_EStringToStringMapEntry> presentation_estringtostringmapentrys,        ArrayList<presentation_EStringToStringMapEntry> presentation_estringtostringmapentrys    ) {
        this.mixed = mixed;
        this.presentation_composites = presentation_composites;
        this.presentation_estringtostringmapentrys = presentation_estringtostringmapentrys;
        this.presentation_estringtostringmapentrys = presentation_estringtostringmapentrys;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<presentation_Composite> getPresentation_composites() {
        return presentation_composites;
    }

    public void addPresentation_composite(Presentation_composite presentation_composite) {
        this.presentation_composites.add(presentation_composite);
    }
    public List<presentation_EStringToStringMapEntry> getPresentation_estringtostringmapentrys() {
        return presentation_estringtostringmapentrys;
    }

    public void addPresentation_estringtostringmapentry(Presentation_estringtostringmapentry presentation_estringtostringmapentry) {
        this.presentation_estringtostringmapentrys.add(presentation_estringtostringmapentry);
    }
    public List<presentation_EStringToStringMapEntry> getPresentation_estringtostringmapentrys() {
        return presentation_estringtostringmapentrys;
    }

    public void addPresentation_estringtostringmapentry(Presentation_estringtostringmapentry presentation_estringtostringmapentry) {
        this.presentation_estringtostringmapentrys.add(presentation_estringtostringmapentry);
    }

}