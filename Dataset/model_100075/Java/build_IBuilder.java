





import java.util.List;
import java.util.ArrayList;

public class build_IBuilder extends IProvidedCapabilityContainer, IFunction {

    private String unitType;





    private build_BPropertySet build_bpropertyset;




    private build_BuildUnit build_buildunit;




    private build_UnitParameterDeclaration build_unitparameterdeclaration;


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

    public build_BPropertySet getBuild_bpropertyset() {
        return build_bpropertyset;
    }

    public void setBuild_bpropertyset(build_BPropertySet build_bpropertyset) {
        this.build_bpropertyset = build_bpropertyset;
    }
    public build_BuildUnit getBuild_buildunit() {
        return build_buildunit;
    }

    public void setBuild_buildunit(build_BuildUnit build_buildunit) {
        this.build_buildunit = build_buildunit;
    }
    public build_UnitParameterDeclaration getBuild_unitparameterdeclaration() {
        return build_unitparameterdeclaration;
    }

    public void setBuild_unitparameterdeclaration(build_UnitParameterDeclaration build_unitparameterdeclaration) {
        this.build_unitparameterdeclaration = build_unitparameterdeclaration;
    }

}