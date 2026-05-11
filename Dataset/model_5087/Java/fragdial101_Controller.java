





import java.util.List;
import java.util.ArrayList;

public class fragdial101_Controller  {

    private String language;
    private String descriptor;





    private fragdial101_AbstractComponent fragdial101_abstractcomponent;


    public fragdial101_Controller(
        String language,        String descriptor    ) {
        this.language = language;
        this.descriptor = descriptor;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getDescriptor() {
        return descriptor;
    }

    public void setDescriptor(String descriptor) {
        this.descriptor = descriptor;
    }

    public fragdial101_AbstractComponent getFragdial101_abstractcomponent() {
        return fragdial101_abstractcomponent;
    }

    public void setFragdial101_abstractcomponent(fragdial101_AbstractComponent fragdial101_abstractcomponent) {
        this.fragdial101_abstractcomponent = fragdial101_abstractcomponent;
    }

}