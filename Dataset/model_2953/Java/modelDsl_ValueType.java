





import java.util.List;
import java.util.ArrayList;

public class modelDsl_ValueType extends ModelType {






    private List<modelDsl_DefAttribute> modeldsl_defattributes;


    public modelDsl_ValueType(
    ) {
        super(
        );
        this.modeldsl_defattributes = new ArrayList<>();
    }

    public modelDsl_ValueType(
        ArrayList<modelDsl_DefAttribute> modeldsl_defattributes    ) {
        this.modeldsl_defattributes = modeldsl_defattributes;
    }


    public List<modelDsl_DefAttribute> getModeldsl_defattributes() {
        return modeldsl_defattributes;
    }

    public void addModeldsl_defattribute(Modeldsl_defattribute modeldsl_defattribute) {
        this.modeldsl_defattributes.add(modeldsl_defattribute);
    }

}