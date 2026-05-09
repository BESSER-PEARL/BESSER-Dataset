





import java.util.List;
import java.util.ArrayList;

public class MessageDefinition  {






    private HALL_FSMActions_Enable hall_fsmactions_enable;




    private HALL_Data hall_data;




    private HALL_Model hall_model;




    private HALL_Actions_Enable hall_actions_enable;


    public MessageDefinition(
    ) {
    }



    public HALL_FSMActions_Enable getHall_fsmactions_enable() {
        return hall_fsmactions_enable;
    }

    public void setHall_fsmactions_enable(HALL_FSMActions_Enable hall_fsmactions_enable) {
        this.hall_fsmactions_enable = hall_fsmactions_enable;
    }
    public HALL_Data getHall_data() {
        return hall_data;
    }

    public void setHall_data(HALL_Data hall_data) {
        this.hall_data = hall_data;
    }
    public HALL_Model getHall_model() {
        return hall_model;
    }

    public void setHall_model(HALL_Model hall_model) {
        this.hall_model = hall_model;
    }
    public HALL_Actions_Enable getHall_actions_enable() {
        return hall_actions_enable;
    }

    public void setHall_actions_enable(HALL_Actions_Enable hall_actions_enable) {
        this.hall_actions_enable = hall_actions_enable;
    }

}