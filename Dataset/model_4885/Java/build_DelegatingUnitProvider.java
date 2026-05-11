





import java.util.List;
import java.util.ArrayList;

public class build_DelegatingUnitProvider extends UnitProvider {






    private build_UnitProvider build_unitprovider;


    public build_DelegatingUnitProvider(
    ) {
        super(
        );
    }



    public build_UnitProvider getBuild_unitprovider() {
        return build_unitprovider;
    }

    public void setBuild_unitprovider(build_UnitProvider build_unitprovider) {
        this.build_unitprovider = build_unitprovider;
    }

}