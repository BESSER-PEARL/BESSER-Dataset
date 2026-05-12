





import java.util.List;
import java.util.ArrayList;

public class Controller_Controller  {

    private String attribute;
    private None worldAccess;
    private None inputController;
    private None viewAccess;
    private None eventManager;





    private Controller_InputController_Interface controller_inputcontroller_interface;




    private Model_World model_world;




    private View_View view_view;


    public Controller_Controller(
        String attribute,        None worldAccess,        None inputController,        None viewAccess,        None eventManager    ) {
        this.attribute = attribute;
        this.worldAccess = worldAccess;
        this.inputController = inputController;
        this.viewAccess = viewAccess;
        this.eventManager = eventManager;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public None getWorldaccess() {
        return worldAccess;
    }

    public void setWorldaccess(None worldAccess) {
        this.worldAccess = worldAccess;
    }
    public None getInputcontroller() {
        return inputController;
    }

    public void setInputcontroller(None inputController) {
        this.inputController = inputController;
    }
    public None getViewaccess() {
        return viewAccess;
    }

    public void setViewaccess(None viewAccess) {
        this.viewAccess = viewAccess;
    }
    public None getEventmanager() {
        return eventManager;
    }

    public void setEventmanager(None eventManager) {
        this.eventManager = eventManager;
    }

    public Controller_InputController_Interface getController_inputcontroller_interface() {
        return controller_inputcontroller_interface;
    }

    public void setController_inputcontroller_interface(Controller_InputController_Interface controller_inputcontroller_interface) {
        this.controller_inputcontroller_interface = controller_inputcontroller_interface;
    }
    public Model_World getModel_world() {
        return model_world;
    }

    public void setModel_world(Model_World model_world) {
        this.model_world = model_world;
    }
    public View_View getView_view() {
        return view_view;
    }

    public void setView_view(View_View view_view) {
        this.view_view = view_view;
    }

}