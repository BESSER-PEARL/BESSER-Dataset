





import java.util.List;
import java.util.ArrayList;

public class mtl_ModuleElementDocumentation extends Documentation {






    private List<mtl_ParameterDocumentation> mtl_parameterdocumentations;


    public mtl_ModuleElementDocumentation(
    ) {
        super(
        );
        this.mtl_parameterdocumentations = new ArrayList<>();
    }

    public mtl_ModuleElementDocumentation(
        ArrayList<mtl_ParameterDocumentation> mtl_parameterdocumentations    ) {
        this.mtl_parameterdocumentations = mtl_parameterdocumentations;
    }


    public List<mtl_ParameterDocumentation> getMtl_parameterdocumentations() {
        return mtl_parameterdocumentations;
    }

    public void addMtl_parameterdocumentation(Mtl_parameterdocumentation mtl_parameterdocumentation) {
        this.mtl_parameterdocumentations.add(mtl_parameterdocumentation);
    }

}