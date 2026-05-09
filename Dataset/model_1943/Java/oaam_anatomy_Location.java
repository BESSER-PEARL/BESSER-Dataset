





import java.util.List;
import java.util.ArrayList;

public class oaam_anatomy_Location extends library_ResourceProviderInstanceA, common_OaamBaseElementA, scenario_ModeDependentElementA, scenario_VariantDependentElementA {

    private float length;



    public oaam_anatomy_Location(
        float length    ) {
        super(
        );
        this.length = length;
    }


    public float getLength() {
        return length;
    }

    public void setLength(float length) {
        this.length = length;
    }


}