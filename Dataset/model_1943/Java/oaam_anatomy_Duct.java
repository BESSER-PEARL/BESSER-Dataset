





import java.util.List;
import java.util.ArrayList;

public class oaam_anatomy_Duct extends common_OaamBaseElementA, scenario_VariantDependentElementA, scenario_ModeDependentElementA, library_ResourceProviderInstanceA {

    private float length;



    public oaam_anatomy_Duct(
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