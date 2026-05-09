





import java.util.List;
import java.util.ArrayList;

public class oaam_scenario_ScenarioContainerA extends OaamBaseElementA {






    private List<Variant> variants;


    public oaam_scenario_ScenarioContainerA(
    ) {
        super(
        );
        this.variants = new ArrayList<>();
    }

    public oaam_scenario_ScenarioContainerA(
        ArrayList<Variant> variants    ) {
        this.variants = variants;
    }


    public List<Variant> getVariants() {
        return variants;
    }

    public void addVariant(Variant variant) {
        this.variants.add(variant);
    }

}