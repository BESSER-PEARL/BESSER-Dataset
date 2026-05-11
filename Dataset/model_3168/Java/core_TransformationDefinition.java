





import java.util.List;
import java.util.ArrayList;

public class core_TransformationDefinition extends ModuleDefinition {






    private List<core_ImportedModel> core_importedmodels;




    private core_EclecticTransformationDefinition core_eclectictransformationdefinition;




    private List<core_TransformationDefinitionParameter> core_transformationdefinitionparameters;




    private List<core_TransformationDefinitionParameter> core_transformationdefinitionparameters;




    private List<core_Annotation> core_annotations;




    private List<core_InlineModel> core_inlinemodels;




    private List<core_UseDeclaration> core_usedeclarations;




    private List<core_RequireDeclaration> core_requiredeclarations;


    public core_TransformationDefinition(
    ) {
        super(
        );
        this.core_importedmodels = new ArrayList<>();
        this.core_transformationdefinitionparameters = new ArrayList<>();
        this.core_transformationdefinitionparameters = new ArrayList<>();
        this.core_annotations = new ArrayList<>();
        this.core_inlinemodels = new ArrayList<>();
        this.core_usedeclarations = new ArrayList<>();
        this.core_requiredeclarations = new ArrayList<>();
    }

    public core_TransformationDefinition(
        ArrayList<core_ImportedModel> core_importedmodels,        ArrayList<core_TransformationDefinitionParameter> core_transformationdefinitionparameters,        ArrayList<core_TransformationDefinitionParameter> core_transformationdefinitionparameters,        ArrayList<core_Annotation> core_annotations,        ArrayList<core_InlineModel> core_inlinemodels,        ArrayList<core_UseDeclaration> core_usedeclarations,        ArrayList<core_RequireDeclaration> core_requiredeclarations    ) {
        this.core_importedmodels = core_importedmodels;
        this.core_transformationdefinitionparameters = core_transformationdefinitionparameters;
        this.core_transformationdefinitionparameters = core_transformationdefinitionparameters;
        this.core_annotations = core_annotations;
        this.core_inlinemodels = core_inlinemodels;
        this.core_usedeclarations = core_usedeclarations;
        this.core_requiredeclarations = core_requiredeclarations;
    }


    public List<core_ImportedModel> getCore_importedmodels() {
        return core_importedmodels;
    }

    public void addCore_importedmodel(Core_importedmodel core_importedmodel) {
        this.core_importedmodels.add(core_importedmodel);
    }
    public core_EclecticTransformationDefinition getCore_eclectictransformationdefinition() {
        return core_eclectictransformationdefinition;
    }

    public void setCore_eclectictransformationdefinition(core_EclecticTransformationDefinition core_eclectictransformationdefinition) {
        this.core_eclectictransformationdefinition = core_eclectictransformationdefinition;
    }
    public List<core_TransformationDefinitionParameter> getCore_transformationdefinitionparameters() {
        return core_transformationdefinitionparameters;
    }

    public void addCore_transformationdefinitionparameter(Core_transformationdefinitionparameter core_transformationdefinitionparameter) {
        this.core_transformationdefinitionparameters.add(core_transformationdefinitionparameter);
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
    public List<core_InlineModel> getCore_inlinemodels() {
        return core_inlinemodels;
    }

    public void addCore_inlinemodel(Core_inlinemodel core_inlinemodel) {
        this.core_inlinemodels.add(core_inlinemodel);
    }
    public List<core_UseDeclaration> getCore_usedeclarations() {
        return core_usedeclarations;
    }

    public void addCore_usedeclaration(Core_usedeclaration core_usedeclaration) {
        this.core_usedeclarations.add(core_usedeclaration);
    }
    public List<core_RequireDeclaration> getCore_requiredeclarations() {
        return core_requiredeclarations;
    }

    public void addCore_requiredeclaration(Core_requiredeclaration core_requiredeclaration) {
        this.core_requiredeclarations.add(core_requiredeclaration);
    }

}