





import java.util.List;
import java.util.ArrayList;

public class model_SymbolReference extends Primitive {

    private String onCreateProperties;
    private String uri;
    private String zoom;



    public model_SymbolReference(
        String onCreateProperties,        String uri,        String zoom    ) {
        super(
        );
        this.onCreateProperties = onCreateProperties;
        this.uri = uri;
        this.zoom = zoom;
    }


    public String getOncreateproperties() {
        return onCreateProperties;
    }

    public void setOncreateproperties(String onCreateProperties) {
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


}