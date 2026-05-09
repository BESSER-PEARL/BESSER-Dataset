





import java.util.List;
import java.util.ArrayList;

public class type_ProcessingInstruction  {

    private String target;
    private String data;



    public type_ProcessingInstruction(
        String target,        String data    ) {
        this.target = target;
        this.data = data;
    }


    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }


}