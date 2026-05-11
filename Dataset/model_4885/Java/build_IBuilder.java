





import java.util.List;
import java.util.ArrayList;

public class build_IBuilder extends IFunction, IProvidedCapabilityContainer {

    private String unitType;





    private build_BuildUnit build_buildunit;


    public build_IBuilder(
        String unitType    ) {
        super(
        );
        this.unitType = unitType;
    }


    public String getUnittype() {
        return unitType;
    }

    public void setUnittype(String unitType) {
        this.unitType = unitType;
    }

    public build_BuildUnit getBuild_buildunit() {
        return build_buildunit;
    }

    public void setBuild_buildunit(build_BuildUnit build_buildunit) {
        this.build_buildunit = build_buildunit;
    }

}