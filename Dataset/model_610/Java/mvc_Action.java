





import java.util.List;
import java.util.ArrayList;

public class mvc_Action extends Annotable {

    private String name;





    private mvc_Controller mvc_controller;


    public mvc_Action(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mvc_Controller getMvc_controller() {
        return mvc_controller;
    }

    public void setMvc_controller(mvc_Controller mvc_controller) {
        this.mvc_controller = mvc_controller;
    }

}