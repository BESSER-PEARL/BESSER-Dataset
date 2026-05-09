





import java.util.List;
import java.util.ArrayList;

public class oaam_scenario_VariantDependentElementA  {






    private List<Variant> variants;


    public oaam_scenario_VariantDependentElementA(
    ) {
        this.variants = new ArrayList<>();
    }

    public oaam_scenario_VariantDependentElementA(
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