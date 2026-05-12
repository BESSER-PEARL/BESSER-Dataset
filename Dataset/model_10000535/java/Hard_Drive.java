





import java.util.List;
import java.util.ArrayList;

public class Hard_Drive  {

    private String memory;





    private Operating_System operating_system;




    private Request request;


    public Hard_Drive(
        String memory    ) {
        this.memory = memory;
    }


    public String getMemory() {
        return memory;
    }

    public void setMemory(String memory) {
        this.memory = memory;
    }

    public Operating_System getOperating_system() {
        return operating_system;
    }

    public void setOperating_system(Operating_System operating_system) {
        this.operating_system = operating_system;
    }
    public Request getRequest() {
        return request;
    }

    public void setRequest(Request request) {
        this.request = request;
    }

}