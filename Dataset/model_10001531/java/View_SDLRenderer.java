





import java.util.List;
import java.util.ArrayList;

public class View_SDLRenderer  {

    private String renderer;
    private None viewPointer;
    private None camera;
    private String window;
    private None tileset;





    private View_Renderer_Interface view_renderer_interface;


    public View_SDLRenderer(
        String renderer,        None viewPointer,        None camera,        String window,        None tileset    ) {
        this.renderer = renderer;
        this.viewPointer = viewPointer;
        this.camera = camera;
        this.window = window;
        this.tileset = tileset;
    }


    public String getRenderer() {
        return renderer;
    }

    public void setRenderer(String renderer) {
        this.renderer = renderer;
    }
    public None getViewpointer() {
        return viewPointer;
    }

    public void setViewpointer(None viewPointer) {
        this.viewPointer = viewPointer;
    }
    public None getCamera() {
        return camera;
    }

    public void setCamera(None camera) {
        this.camera = camera;
    }
    public String getWindow() {
        return window;
    }

    public void setWindow(String window) {
        this.window = window;
    }
    public None getTileset() {
        return tileset;
    }

    public void setTileset(None tileset) {
        this.tileset = tileset;
    }

    public View_Renderer_Interface getView_renderer_interface() {
        return view_renderer_interface;
    }

    public void setView_renderer_interface(View_Renderer_Interface view_renderer_interface) {
        this.view_renderer_interface = view_renderer_interface;
    }

}