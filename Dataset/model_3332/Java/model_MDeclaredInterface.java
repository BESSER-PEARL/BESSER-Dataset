





import java.util.List;
import java.util.ArrayList;

public class model_MDeclaredInterface extends AbstractMInterface, AbstractMDeclaredType {






    private List<model_AbstractMInterface> model_abstractminterfaces;


    public model_MDeclaredInterface(
    ) {
        super(
        );
        this.model_abstractminterfaces = new ArrayList<>();
    }

    public model_MDeclaredInterface(
        ArrayList<model_AbstractMInterface> model_abstractminterfaces    ) {
        this.model_abstractminterfaces = model_abstractminterfaces;
    }


    public List<model_AbstractMInterface> getModel_abstractminterfaces() {
        return model_abstractminterfaces;
    }

    public void addModel_abstractminterface(Model_abstractminterface model_abstractminterface) {
        this.model_abstractminterfaces.add(model_abstractminterface);
    }

}