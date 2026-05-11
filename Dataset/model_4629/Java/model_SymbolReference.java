





import java.util.List;
import java.util.ArrayList;

public class model_SymbolReference extends Primitive {

    private String zoom;
    private String onCreateProperties;
    private String uri;



    public model_SymbolReference(
        String zoom,        String onCreateProperties,        String uri    ) {
        super(
        );
        this.zoom = zoom;
        this.onCreateProperties = onCreateProperties;
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
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }


}