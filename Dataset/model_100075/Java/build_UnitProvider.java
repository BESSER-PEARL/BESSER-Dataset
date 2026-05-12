





import java.util.List;
import java.util.ArrayList;

public class build_UnitProvider extends BExpression {

    private String documentation;





    private build_CompoundUnitProvider build_compoundunitprovider;


    public build_UnitProvider(
        String documentation    ) {
        super(
        );
        this.documentation = documentation;
    }


    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }

    public build_CompoundUnitProvider getBuild_compoundunitprovider() {
        return build_compoundunitprovider;
    }

    public void setBuild_compoundunitprovider(build_CompoundUnitProvider build_compoundunitprovider) {
        this.build_compoundunitprovider = build_compoundunitprovider;
    }

}