





import java.util.List;
import java.util.ArrayList;

public class model_SymbolReference extends Primitive {

    private String uri;
    private String zoom;
    private String onCreateProperties;





    private List<model_StringToStringMap> model_stringtostringmaps;


    public model_SymbolReference(
        String uri,        String zoom,        String onCreateProperties    ) {
        super(
        );
        this.uri = uri;
        this.zoom = zoom;
        this.onCreateProperties = onCreateProperties;
        this.model_stringtostringmaps = new ArrayList<>();
    }

    public model_SymbolReference(
        String uri,        String zoom,        String onCreateProperties        ArrayList<model_StringToStringMap> model_stringtostringmaps    ) {
        this.uri = uri;
        this.zoom = zoom;
        this.onCreateProperties = onCreateProperties;
        this.model_stringtostringmaps = model_stringtostringmaps;
    }

    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }
    public String getZoom() {
        return zoom;
    }

    public void setZoom(String zoom) {
        this.zoom = zoom;
    }
    public String getOncreateproperties() {
        return onCreateProperties;
    }

    public void setOncreateproperties(String onCreateProperties) {
        this.onCreateProperties = onCreateProperties;
    }

    public List<model_StringToStringMap> getModel_stringtostringmaps() {
        return model_stringtostringmaps;
    }

    public void addModel_stringtostringmap(Model_stringtostringmap model_stringtostringmap) {
        this.model_stringtostringmaps.add(model_stringtostringmap);
    }

}