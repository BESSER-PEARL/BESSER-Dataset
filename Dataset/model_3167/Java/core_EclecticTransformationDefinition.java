





import java.util.List;
import java.util.ArrayList;

public class core_EclecticTransformationDefinition extends TransformationDefinition {






    private List<core_TransformationDefinition> core_transformationdefinitions;


    public core_EclecticTransformationDefinition(
    ) {
        super(
        );
        this.core_transformationdefinitions = new ArrayList<>();
    }

    public core_EclecticTransformationDefinition(
        ArrayList<core_TransformationDefinition> core_transformationdefinitions    ) {
        this.core_transformationdefinitions = core_transformationdefinitions;
    }


    public List<core_TransformationDefinition> getCore_transformationdefinitions() {
        return core_transformationdefinitions;
    }

    public void addCore_transformationdefinition(Core_transformationdefinition core_transformationdefinition) {
        this.core_transformationdefinitions.add(core_transformationdefinition);
    }

}