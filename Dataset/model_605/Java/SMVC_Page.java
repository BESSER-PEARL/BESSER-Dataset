





import java.util.List;
import java.util.ArrayList;

public class SMVC_Page  {

    private String title;





    private SMVC_Controller smvc_controller;


    public SMVC_Page(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public SMVC_Controller getSmvc_controller() {
        return smvc_controller;
    }

    public void setSmvc_controller(SMVC_Controller smvc_controller) {
        this.smvc_controller = smvc_controller;
    }

}