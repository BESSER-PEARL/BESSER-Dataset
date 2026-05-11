





import java.util.List;
import java.util.ArrayList;

public class Model_DEVS  {

    private String name;





    private Model_DEVS model_devs;




    private List<Model_IPort> model_iports;




    private List<Model_OPort> model_oports;


    public Model_DEVS(
        String name    ) {
        this.name = name;
        this.model_iports = new ArrayList<>();
        this.model_oports = new ArrayList<>();
    }

    public Model_DEVS(
        String name        ArrayList<Model_IPort> model_iports,        ArrayList<Model_OPort> model_oports    ) {
        this.name = name;
        this.model_iports = model_iports;
        this.model_oports = model_oports;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Model_DEVS getModel_devs() {
        return model_devs;
    }

    public void setModel_devs(Model_DEVS model_devs) {
        this.model_devs = model_devs;
    }
    public List<Model_IPort> getModel_iports() {
        return model_iports;
    }

    public void addModel_iport(Model_iport model_iport) {
        this.model_iports.add(model_iport);
    }
    public List<Model_OPort> getModel_oports() {
        return model_oports;
    }

    public void addModel_oport(Model_oport model_oport) {
        this.model_oports.add(model_oport);
    }

}