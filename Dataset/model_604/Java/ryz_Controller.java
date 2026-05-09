





import java.util.List;
import java.util.ArrayList;

public class ryz_Controller extends MainComponent {






    private List<ryz_ActionMethod> ryz_actionmethods;




    private ryz_ControllerPackage ryz_controllerpackage;


    public ryz_Controller(
    ) {
        super(
        );
        this.ryz_actionmethods = new ArrayList<>();
    }

    public ryz_Controller(
        ArrayList<ryz_ActionMethod> ryz_actionmethods    ) {
        this.ryz_actionmethods = ryz_actionmethods;
    }


    public List<ryz_ActionMethod> getRyz_actionmethods() {
        return ryz_actionmethods;
    }

    public void addRyz_actionmethod(Ryz_actionmethod ryz_actionmethod) {
        this.ryz_actionmethods.add(ryz_actionmethod);
    }
    public ryz_ControllerPackage getRyz_controllerpackage() {
        return ryz_controllerpackage;
    }

    public void setRyz_controllerpackage(ryz_ControllerPackage ryz_controllerpackage) {
        this.ryz_controllerpackage = ryz_controllerpackage;
    }

}