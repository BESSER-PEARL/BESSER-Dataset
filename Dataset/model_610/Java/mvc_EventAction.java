





import java.util.List;
import java.util.ArrayList;

public class mvc_EventAction extends Annotable {






    private mvc_Controller mvc_controller;




    private mvc_Action mvc_action;


    public mvc_EventAction(
    ) {
        super(
        );
    }



    public mvc_Controller getMvc_controller() {
        return mvc_controller;
    }

    public void setMvc_controller(mvc_Controller mvc_controller) {
        this.mvc_controller = mvc_controller;
    }
    public mvc_Action getMvc_action() {
        return mvc_action;
    }

    public void setMvc_action(mvc_Action mvc_action) {
        this.mvc_action = mvc_action;
    }

}