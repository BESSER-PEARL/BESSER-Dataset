





import java.util.List;
import java.util.ArrayList;

public class model_MDeclaredClass extends AbstractMDeclaredType, AbstractMClass {






    private List<model_AbstractMInterface> model_abstractminterfaces;




    private model_AbstractMClass model_abstractmclass;


    public model_MDeclaredClass(
    ) {
        super(
        );
        this.model_abstractminterfaces = new ArrayList<>();
    }

    public model_MDeclaredClass(
        ArrayList<model_AbstractMInterface> model_abstractminterfaces    ) {
        this.model_abstractminterfaces = model_abstractminterfaces;
    }


    public List<model_AbstractMInterface> getModel_abstractminterfaces() {
        return model_abstractminterfaces;
    }

    public void addModel_abstractminterface(Model_abstractminterface model_abstractminterface) {
        this.model_abstractminterfaces.add(model_abstractminterface);
    }
    public model_AbstractMClass getModel_abstractmclass() {
        return model_abstractmclass;
    }

    public void setModel_abstractmclass(model_AbstractMClass model_abstractmclass) {
        this.model_abstractmclass = model_abstractmclass;
    }

}