





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_SymbolReference extends Primitive {

    private String onCreateProperties;
    private String zoom;
    private String uri;





    private List<VisualInterface_StringToStringMap> visualinterface_stringtostringmaps;


    public VisualInterface_SymbolReference(
        String onCreateProperties,        String zoom,        String uri    ) {
        super(
        );
        this.onCreateProperties = onCreateProperties;
        this.zoom = zoom;
        this.uri = uri;
        this.visualinterface_stringtostringmaps = new ArrayList<>();
    }

    public VisualInterface_SymbolReference(
        String onCreateProperties,        String zoom,        String uri        ArrayList<VisualInterface_StringToStringMap> visualinterface_stringtostringmaps    ) {
        this.onCreateProperties = onCreateProperties;
        this.zoom = zoom;
        this.uri = uri;
        this.visualinterface_stringtostringmaps = visualinterface_stringtostringmaps;
    }

    public String getOncreateproperties() {
        return onCreateProperties;
    }

    public void setOncreateproperties(String onCreateProperties) {
        this.onCreateProperties = onCreateProperties;
    }
    public String getZoom() {
        return zoom;
    }

    public void setZoom(String zoom) {
        this.zoom = zoom;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }

    public List<VisualInterface_StringToStringMap> getVisualinterface_stringtostringmaps() {
        return visualinterface_stringtostringmaps;
    }

    public void addVisualinterface_stringtostringmap(Visualinterface_stringtostringmap visualinterface_stringtostringmap) {
        this.visualinterface_stringtostringmaps.add(visualinterface_stringtostringmap);
    }

}