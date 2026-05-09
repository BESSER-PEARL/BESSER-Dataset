





import java.util.List;
import java.util.ArrayList;

public class gbind_dsl_BindingModel  {

    private String name;
    private boolean targetBinding;



    public gbind_dsl_BindingModel(
        String name,        boolean targetBinding    ) {
        this.name = name;
        this.targetBinding = targetBinding;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getTargetbinding() {
        return targetBinding;
    }

    public void setTargetbinding(boolean targetBinding) {
        this.targetBinding = targetBinding;
    }


}