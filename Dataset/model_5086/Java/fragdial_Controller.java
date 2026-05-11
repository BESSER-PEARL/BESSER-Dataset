





import java.util.List;
import java.util.ArrayList;

public class fragdial_Controller  {

    private String descriptor;
    private String language;





    private fragdial_AbstractComponent fragdial_abstractcomponent;


    public fragdial_Controller(
        String descriptor,        String language    ) {
        this.descriptor = descriptor;
        this.language = language;
    }


    public String getDescriptor() {
        return descriptor;
    }

    public void setDescriptor(String descriptor) {
        this.descriptor = descriptor;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public fragdial_AbstractComponent getFragdial_abstractcomponent() {
        return fragdial_abstractcomponent;
    }

    public void setFragdial_abstractcomponent(fragdial_AbstractComponent fragdial_abstractcomponent) {
        this.fragdial_abstractcomponent = fragdial_abstractcomponent;
    }

}