





import java.util.List;
import java.util.ArrayList;

public class model_Sample  {






    private List<model_Quantity> model_quantitys;




    private model_Sampling model_sampling;


    public model_Sample(
    ) {
        this.model_quantitys = new ArrayList<>();
    }

    public model_Sample(
        ArrayList<model_Quantity> model_quantitys    ) {
        this.model_quantitys = model_quantitys;
    }


    public List<model_Quantity> getModel_quantitys() {
        return model_quantitys;
    }

    public void addModel_quantity(Model_quantity model_quantity) {
        this.model_quantitys.add(model_quantity);
    }
    public model_Sampling getModel_sampling() {
        return model_sampling;
    }

    public void setModel_sampling(model_Sampling model_sampling) {
        this.model_sampling = model_sampling;
    }

}