





import java.util.List;
import java.util.ArrayList;

public class backbone_RouterMapping  {

    private String path;





    private backbone_Router backbone_router;




    private backbone_View backbone_view;


    public backbone_RouterMapping(
        String path    ) {
        this.path = path;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }

    public backbone_Router getBackbone_router() {
        return backbone_router;
    }

    public void setBackbone_router(backbone_Router backbone_router) {
        this.backbone_router = backbone_router;
    }
    public backbone_View getBackbone_view() {
        return backbone_view;
    }

    public void setBackbone_view(backbone_View backbone_view) {
        this.backbone_view = backbone_view;
    }

}