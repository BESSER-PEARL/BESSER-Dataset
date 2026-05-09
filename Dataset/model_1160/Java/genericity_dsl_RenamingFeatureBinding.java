





import java.util.List;
import java.util.ArrayList;

public class genericity_dsl_RenamingFeatureBinding extends BaseFeatureBinding {

    private String concreteFeature;



    public genericity_dsl_RenamingFeatureBinding(
        String concreteFeature    ) {
        super(
        );
        this.concreteFeature = concreteFeature;
    }


    public String getConcretefeature() {
        return concreteFeature;
    }

    public void setConcretefeature(String concreteFeature) {
        this.concreteFeature = concreteFeature;
    }


}