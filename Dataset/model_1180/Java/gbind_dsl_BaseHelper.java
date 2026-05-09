





import java.util.List;
import java.util.ArrayList;

public class gbind_dsl_BaseHelper  {

    private String feature;





    private BindingModel bindingmodel;


    public gbind_dsl_BaseHelper(
        String feature    ) {
        this.feature = feature;
    }


    public String getFeature() {
        return feature;
    }

    public void setFeature(String feature) {
        this.feature = feature;
    }

    public BindingModel getBindingmodel() {
        return bindingmodel;
    }

    public void setBindingmodel(BindingModel bindingmodel) {
        this.bindingmodel = bindingmodel;
    }

}