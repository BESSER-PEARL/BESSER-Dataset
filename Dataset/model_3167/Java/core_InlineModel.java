





import java.util.List;
import java.util.ArrayList;

public class core_InlineModel extends RepresentModel, ModuleDefinition {






    private List<core_InlineClass> core_inlineclasss;




    private core_TransformationDefinition core_transformationdefinition;


    public core_InlineModel(
    ) {
        super(
        );
        this.core_inlineclasss = new ArrayList<>();
    }

    public core_InlineModel(
        ArrayList<core_InlineClass> core_inlineclasss    ) {
        this.core_inlineclasss = core_inlineclasss;
    }


    public List<core_InlineClass> getCore_inlineclasss() {
        return core_inlineclasss;
    }

    public void addCore_inlineclass(Core_inlineclass core_inlineclass) {
        this.core_inlineclasss.add(core_inlineclass);
    }
    public core_TransformationDefinition getCore_transformationdefinition() {
        return core_transformationdefinition;
    }

    public void setCore_transformationdefinition(core_TransformationDefinition core_transformationdefinition) {
        this.core_transformationdefinition = core_transformationdefinition;
    }

}