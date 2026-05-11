





import java.util.List;
import java.util.ArrayList;

public class micro_AggregateService extends Service {






    private List<micro_Model> micro_models;




    private micro_Operation micro_operation;




    private micro_API micro_api;




    private micro_ModelEvent micro_modelevent;




    private List<micro_Operation> micro_operations;




    private List<micro_ModelEvent> micro_modelevents;




    private micro_ViewService micro_viewservice;




    private List<micro_ModelEvent> micro_modelevents;


    public micro_AggregateService(
    ) {
        super(
        );
        this.micro_models = new ArrayList<>();
        this.micro_operations = new ArrayList<>();
        this.micro_modelevents = new ArrayList<>();
        this.micro_modelevents = new ArrayList<>();
    }

    public micro_AggregateService(
        ArrayList<micro_Model> micro_models,        ArrayList<micro_Operation> micro_operations,        ArrayList<micro_ModelEvent> micro_modelevents,        ArrayList<micro_ModelEvent> micro_modelevents    ) {
        this.micro_models = micro_models;
        this.micro_operations = micro_operations;
        this.micro_modelevents = micro_modelevents;
        this.micro_modelevents = micro_modelevents;
    }


    public List<micro_Model> getMicro_models() {
        return micro_models;
    }

    public void addMicro_model(Micro_model micro_model) {
        this.micro_models.add(micro_model);
    }
    public micro_Operation getMicro_operation() {
        return micro_operation;
    }

    public void setMicro_operation(micro_Operation micro_operation) {
        this.micro_operation = micro_operation;
    }
    public micro_API getMicro_api() {
        return micro_api;
    }

    public void setMicro_api(micro_API micro_api) {
        this.micro_api = micro_api;
    }
    public micro_ModelEvent getMicro_modelevent() {
        return micro_modelevent;
    }

    public void setMicro_modelevent(micro_ModelEvent micro_modelevent) {
        this.micro_modelevent = micro_modelevent;
    }
    public List<micro_Operation> getMicro_operations() {
        return micro_operations;
    }

    public void addMicro_operation(Micro_operation micro_operation) {
        this.micro_operations.add(micro_operation);
    }
    public List<micro_ModelEvent> getMicro_modelevents() {
        return micro_modelevents;
    }

    public void addMicro_modelevent(Micro_modelevent micro_modelevent) {
        this.micro_modelevents.add(micro_modelevent);
    }
    public micro_ViewService getMicro_viewservice() {
        return micro_viewservice;
    }

    public void setMicro_viewservice(micro_ViewService micro_viewservice) {
        this.micro_viewservice = micro_viewservice;
    }
    public List<micro_ModelEvent> getMicro_modelevents() {
        return micro_modelevents;
    }

    public void addMicro_modelevent(Micro_modelevent micro_modelevent) {
        this.micro_modelevents.add(micro_modelevent);
    }

}