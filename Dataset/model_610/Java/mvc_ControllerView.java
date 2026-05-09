





import java.util.List;
import java.util.ArrayList;

public class mvc_ControllerView extends Annotable {






    private List<mvc_Model> mvc_models;




    private mvc_Controller mvc_controller;


    public mvc_ControllerView(
    ) {
        super(
        );
        this.mvc_models = new ArrayList<>();
    }

    public mvc_ControllerView(
        ArrayList<mvc_Model> mvc_models    ) {
        this.mvc_models = mvc_models;
    }


    public List<mvc_Model> getMvc_models() {
        return mvc_models;
    }

    public void addMvc_model(Mvc_model mvc_model) {
        this.mvc_models.add(mvc_model);
    }
    public mvc_Controller getMvc_controller() {
        return mvc_controller;
    }

    public void setMvc_controller(mvc_Controller mvc_controller) {
        this.mvc_controller = mvc_controller;
    }

}