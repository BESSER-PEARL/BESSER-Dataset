





import java.util.List;
import java.util.ArrayList;

public class model_TestContainer extends TestElement {






    private model_TestElement model_testelement;




    private List<model_TestElement> model_testelements;


    public model_TestContainer(
    ) {
        super(
        );
        this.model_testelements = new ArrayList<>();
    }

    public model_TestContainer(
        ArrayList<model_TestElement> model_testelements    ) {
        this.model_testelements = model_testelements;
    }


    public model_TestElement getModel_testelement() {
        return model_testelement;
    }

    public void setModel_testelement(model_TestElement model_testelement) {
        this.model_testelement = model_testelement;
    }
    public List<model_TestElement> getModel_testelements() {
        return model_testelements;
    }

    public void addModel_testelement(Model_testelement model_testelement) {
        this.model_testelements.add(model_testelement);
    }

}