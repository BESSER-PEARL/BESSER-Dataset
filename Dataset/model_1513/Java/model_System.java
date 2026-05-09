





import java.util.List;
import java.util.ArrayList;

public class model_System  {






    private List<model_Buffer> model_buffers;




    private List<model_FSM> model_fsms;


    public model_System(
    ) {
        this.model_buffers = new ArrayList<>();
        this.model_fsms = new ArrayList<>();
    }

    public model_System(
        ArrayList<model_Buffer> model_buffers,        ArrayList<model_FSM> model_fsms    ) {
        this.model_buffers = model_buffers;
        this.model_fsms = model_fsms;
    }


    public List<model_Buffer> getModel_buffers() {
        return model_buffers;
    }

    public void addModel_buffer(Model_buffer model_buffer) {
        this.model_buffers.add(model_buffer);
    }
    public List<model_FSM> getModel_fsms() {
        return model_fsms;
    }

    public void addModel_fsm(Model_fsm model_fsm) {
        this.model_fsms.add(model_fsm);
    }

}