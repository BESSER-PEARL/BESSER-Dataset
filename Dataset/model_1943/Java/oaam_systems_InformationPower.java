





import java.util.List;
import java.util.ArrayList;

public class oaam_systems_InformationPower extends common_OaamBaseElementA, scenario_ModeDependentElementA, systems_ProvidedInformationA, scenario_VariantDependentElementA, systems_RequiredInformationA {

    private float power;



    public oaam_systems_InformationPower(
        float power    ) {
        super(
        );
        this.power = power;
    }


    public float getPower() {
        return power;
    }

    public void setPower(float power) {
        this.power = power;
    }


}