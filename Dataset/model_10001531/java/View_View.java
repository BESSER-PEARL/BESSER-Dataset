





import java.util.List;
import java.util.ArrayList;

public class View_View  {

    private None worldAccess;
    private None renderer;





    private Model_World model_world;


    public View_View(
        None worldAccess,        None renderer    ) {
        this.worldAccess = worldAccess;
        this.renderer = renderer;
    }


    public None getWorldaccess() {
        return worldAccess;
    }

    public void setWorldaccess(None worldAccess) {
        this.worldAccess = worldAccess;
    }
    public None getRenderer() {
        return renderer;
    }

    public void setRenderer(None renderer) {
        this.renderer = renderer;
    }

    public Model_World getModel_world() {
        return model_world;
    }

    public void setModel_world(Model_World model_world) {
        this.model_world = model_world;
    }

}