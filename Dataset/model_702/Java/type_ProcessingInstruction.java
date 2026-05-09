





import java.util.List;
import java.util.ArrayList;

public class type_ProcessingInstruction  {

    private String data;
    private String target;



    public type_ProcessingInstruction(
        String data,        String target    ) {
        this.data = data;
        this.target = target;
    }


    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }


}