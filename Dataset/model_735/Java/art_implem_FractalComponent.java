





import java.util.List;
import java.util.ArrayList;

public class art_implem_FractalComponent extends ComponentImplementation {

    private String controllerDesc;
    private String contentDesc;



    public art_implem_FractalComponent(
        String controllerDesc,        String contentDesc    ) {
        super(
        );
        this.controllerDesc = controllerDesc;
        this.contentDesc = contentDesc;
    }


    public String getControllerdesc() {
        return controllerDesc;
    }

    public void setControllerdesc(String controllerDesc) {
        this.controllerDesc = controllerDesc;
    }
    public String getContentdesc() {
        return contentDesc;
    }

    public void setContentdesc(String contentDesc) {
        this.contentDesc = contentDesc;
    }


}