





import java.util.List;
import java.util.ArrayList;

public class types_ComplexType extends ParameterizedType {






    private List<types_Feature> types_features;




    private types_ComplexType types_complextype;




    private types_Feature types_feature;


    public types_ComplexType(
    ) {
        super(
        );
        this.types_features = new ArrayList<>();
    }

    public types_ComplexType(
        ArrayList<types_Feature> types_features    ) {
        this.types_features = types_features;
    }


    public List<types_Feature> getTypes_features() {
        return types_features;
    }

    public void addTypes_feature(Types_feature types_feature) {
        this.types_features.add(types_feature);
    }
    public types_ComplexType getTypes_complextype() {
        return types_complextype;
    }

    public void setTypes_complextype(types_ComplexType types_complextype) {
        this.types_complextype = types_complextype;
    }
    public types_Feature getTypes_feature() {
        return types_feature;
    }

    public void setTypes_feature(types_Feature types_feature) {
        this.types_feature = types_feature;
    }

}