





import java.util.List;
import java.util.ArrayList;

public class micro_AggregateService extends Service {






    private micro_API micro_api;




    private micro_Operation micro_operation;




    private micro_Model micro_model;




    private List<micro_Model> micro_models;




    private List<micro_Operation> micro_operations;


    public micro_AggregateService(
    ) {
        super(
        );
        this.micro_models = new ArrayList<>();
        this.micro_operations = new ArrayList<>();
    }

    public micro_AggregateService(
        ArrayList<micro_Model> micro_models,        ArrayList<micro_Operation> micro_operations    ) {
        this.micro_models = micro_models;
        this.micro_operations = micro_operations;
    }


    public micro_API getMicro_api() {
        return micro_api;
    }

    public void setMicro_api(micro_API micro_api) {
        this.micro_api = micro_api;
    }
    public micro_Operation getMicro_operation() {
        return micro_operation;
    }

    public void setMicro_operation(micro_Operation micro_operation) {
        this.micro_operation = micro_operation;
    }
    public micro_Model getMicro_model() {
        return micro_model;
    }

    public void setMicro_model(micro_Model micro_model) {
        this.micro_model = micro_model;
    }
    public List<micro_Model> getMicro_models() {
        return micro_models;
    }

    public void addMicro_model(Micro_model micro_model) {
        this.micro_models.add(micro_model);
    }
    public List<micro_Operation> getMicro_operations() {
        return micro_operations;
    }

    public void addMicro_operation(Micro_operation micro_operation) {
        this.micro_operations.add(micro_operation);
    }

}