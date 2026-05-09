





import java.util.List;
import java.util.ArrayList;

public class model_System  {






    private List<model_FSM> model_fsms;




    private List<model_Buffer> model_buffers;


    public model_System(
    ) {
        this.model_fsms = new ArrayList<>();
        this.model_buffers = new ArrayList<>();
    }

    public model_System(
        ArrayList<model_FSM> model_fsms,        ArrayList<model_Buffer> model_buffers    ) {
        this.model_fsms = model_fsms;
        this.model_buffers = model_buffers;
    }


    public List<model_FSM> getModel_fsms() {
        return model_fsms;
    }

    public void addModel_fsm(Model_fsm model_fsm) {
        this.model_fsms.add(model_fsm);
    }
    public List<model_Buffer> getModel_buffers() {
        return model_buffers;
    }

    public void addModel_buffer(Model_buffer model_buffer) {
        this.model_buffers.add(model_buffer);
    }

}