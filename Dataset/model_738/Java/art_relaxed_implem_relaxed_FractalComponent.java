





import java.util.List;
import java.util.ArrayList;

public class art_relaxed_implem_relaxed_FractalComponent extends ComponentImplementation {

    private String contentDesc;
    private String controllerDesc;



    public art_relaxed_implem_relaxed_FractalComponent(
        String contentDesc,        String controllerDesc    ) {
        super(
        );
        this.contentDesc = contentDesc;
        this.controllerDesc = controllerDesc;
    }


    public String getContentdesc() {
        return contentDesc;
    }

    public void setContentdesc(String contentDesc) {
        this.contentDesc = contentDesc;
    }
    public String getControllerdesc() {
        return controllerDesc;
    }

    public void setControllerdesc(String controllerDesc) {
        this.controllerDesc = controllerDesc;
    }


}