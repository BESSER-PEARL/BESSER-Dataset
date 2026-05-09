





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_UnitCS extends CSTNode {






    private List<MappingModuleCS> mappingmodulecss;


    public qvtoperational_cst_UnitCS(
    ) {
        super(
        );
        this.mappingmodulecss = new ArrayList<>();
    }

    public qvtoperational_cst_UnitCS(
        ArrayList<MappingModuleCS> mappingmodulecss    ) {
        this.mappingmodulecss = mappingmodulecss;
    }


    public List<MappingModuleCS> getMappingmodulecss() {
        return mappingmodulecss;
    }

    public void addMappingmodulecs(Mappingmodulecs mappingmodulecs) {
        this.mappingmodulecss.add(mappingmodulecs);
    }

}