





import java.util.List;
import java.util.ArrayList;

public class Routing_Settings  {

    private int Routing_Priority;
    private String Push_Time_Out;
    private None Routing_Model;



    public Routing_Settings(
        int Routing_Priority,        String Push_Time_Out,        None Routing_Model    ) {
        this.Routing_Priority = Routing_Priority;
        this.Push_Time_Out = Push_Time_Out;
        this.Routing_Model = Routing_Model;
    }


    public int getRouting_priority() {
        return Routing_Priority;
    }

    public void setRouting_priority(int Routing_Priority) {
        this.Routing_Priority = Routing_Priority;
    }
    public String getPush_time_out() {
        return Push_Time_Out;
    }

    public void setPush_time_out(String Push_Time_Out) {
        this.Push_Time_Out = Push_Time_Out;
    }
    public None getRouting_model() {
        return Routing_Model;
    }

    public void setRouting_model(None Routing_Model) {
        this.Routing_Model = Routing_Model;
    }


}