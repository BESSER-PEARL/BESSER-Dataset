





import java.util.List;
import java.util.ArrayList;

public class core_RequireDeclaration extends RepresentModel {

    private String default;
    private String name;





    private core_TransformationDefinition core_transformationdefinition;


    public core_RequireDeclaration(
        String default,        String name    ) {
        super(
        );
        this.default = default;
        this.name = name;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public core_TransformationDefinition getCore_transformationdefinition() {
        return core_transformationdefinition;
    }

    public void setCore_transformationdefinition(core_TransformationDefinition core_transformationdefinition) {
        this.core_transformationdefinition = core_transformationdefinition;
    }

}