





import java.util.List;
import java.util.ArrayList;

public class model_PowerBlock  {

    private String name;





    private model_Computer model_computer;


    public model_PowerBlock(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_Computer getModel_computer() {
        return model_computer;
    }

    public void setModel_computer(model_Computer model_computer) {
        this.model_computer = model_computer;
    }

}