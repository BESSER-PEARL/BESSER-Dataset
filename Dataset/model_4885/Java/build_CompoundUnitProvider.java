





import java.util.List;
import java.util.ArrayList;

public class build_CompoundUnitProvider extends UnitProvider {






    private List<build_UnitProvider> build_unitproviders;


    public build_CompoundUnitProvider(
    ) {
        super(
        );
        this.build_unitproviders = new ArrayList<>();
    }

    public build_CompoundUnitProvider(
        ArrayList<build_UnitProvider> build_unitproviders    ) {
        this.build_unitproviders = build_unitproviders;
    }


    public List<build_UnitProvider> getBuild_unitproviders() {
        return build_unitproviders;
    }

    public void addBuild_unitprovider(Build_unitprovider build_unitprovider) {
        this.build_unitproviders.add(build_unitprovider);
    }

}