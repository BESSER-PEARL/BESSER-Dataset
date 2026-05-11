





import java.util.List;
import java.util.ArrayList;

public class core_TransformationDefinition extends ModuleDefinition {






    private List<core_ImportedModel> core_importedmodels;




    private List<core_TransformationDefinitionParameter> core_transformationdefinitionparameters;




    private List<core_Annotation> core_annotations;




    private List<core_TransformationDefinitionParameter> core_transformationdefinitionparameters;


    public core_TransformationDefinition(
    ) {
        super(
        );
        this.core_importedmodels = new ArrayList<>();
        this.core_transformationdefinitionparameters = new ArrayList<>();
        this.core_annotations = new ArrayList<>();
        this.core_transformationdefinitionparameters = new ArrayList<>();
    }

    public core_TransformationDefinition(
        ArrayList<core_ImportedModel> core_importedmodels,        ArrayList<core_TransformationDefinitionParameter> core_transformationdefinitionparameters,        ArrayList<core_Annotation> core_annotations,        ArrayList<core_TransformationDefinitionParameter> core_transformationdefinitionparameters    ) {
        this.core_importedmodels = core_importedmodels;
        this.core_transformationdefinitionparameters = core_transformationdefinitionparameters;
        this.core_annotations = core_annotations;
        this.core_transformationdefinitionparameters = core_transformationdefinitionparameters;
    }


    public List<core_ImportedModel> getCore_importedmodels() {
        return core_importedmodels;
    }

    public void addCore_importedmodel(Core_importedmodel core_importedmodel) {
        this.core_importedmodels.add(core_importedmodel);
    }
    public List<core_TransformationDefinitionParameter> getCore_transformationdefinitionparameters() {
        return core_transformationdefinitionparameters;
    }

    public void addCore_transformationdefinitionparameter(Core_transformationdefinitionparameter core_transformationdefinitionparameter) {
        this.core_transformationdefinitionparameters.add(core_transformationdefinitionparameter);
    }
    public List<core_Annotation> getCore_annotations() {
        return core_annotations;
    }

    public void addCore_annotation(Core_annotation core_annotation) {
        this.core_annotations.add(core_annotation);
    }
    public List<core_TransformationDefinitionParameter> getCore_transformationdefinitionparameters() {
        return core_transformationdefinitionparameters;
    }

    public void addCore_transformationdefinitionparameter(Core_transformationdefinitionparameter core_transformationdefinitionparameter) {
        this.core_transformationdefinitionparameters.add(core_transformationdefinitionparameter);
    }

}