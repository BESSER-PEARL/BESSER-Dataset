





import java.util.List;
import java.util.ArrayList;

public class oaam_systems_InformationMaterial extends common_OaamBaseElementA, scenario_ModeDependentElementA, systems_ProvidedInformationA, scenario_VariantDependentElementA, systems_RequiredInformationA {

    private float velocity;
    private float density;



    public oaam_systems_InformationMaterial(
        float velocity,        float density    ) {
        super(
        );
        this.velocity = velocity;
        this.density = density;
    }


    public float getVelocity() {
        return velocity;
    }

    public void setVelocity(float velocity) {
        this.velocity = velocity;
    }
    public float getDensity() {
        return density;
    }

    public void setDensity(float density) {
        this.density = density;
    }


}