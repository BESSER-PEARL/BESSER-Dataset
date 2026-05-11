





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_SymbolReference extends Primitive {

    private String uri;
    private String zoom;
    private String onCreateProperties;



    public VisualInterface_SymbolReference(
        String uri,        String zoom,        String onCreateProperties    ) {
        super(
        );
        this.uri = uri;
        this.zoom = zoom;
        this.onCreateProperties = onCreateProperties;
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


}