





import java.util.List;
import java.util.ArrayList;

public class frontend_core_TransformationDefinition extends ModuleDefinition {






    private List<Annotation> annotations;




    private List<TransformationDefinitionParameter> transformationdefinitionparameters;




    private List<UseDeclaration> usedeclarations;




    private List<TransformationDefinitionParameter> transformationdefinitionparameters;


    public frontend_core_TransformationDefinition(
    ) {
        super(
        );
        this.annotations = new ArrayList<>();
        this.transformationdefinitionparameters = new ArrayList<>();
        this.usedeclarations = new ArrayList<>();
        this.transformationdefinitionparameters = new ArrayList<>();
    }

    public frontend_core_TransformationDefinition(
        ArrayList<Annotation> annotations,        ArrayList<TransformationDefinitionParameter> transformationdefinitionparameters,        ArrayList<UseDeclaration> usedeclarations,        ArrayList<TransformationDefinitionParameter> transformationdefinitionparameters    ) {
        this.annotations = annotations;
        this.transformationdefinitionparameters = transformationdefinitionparameters;
        this.usedeclarations = usedeclarations;
        this.transformationdefinitionparameters = transformationdefinitionparameters;
    }


    public List<Annotation> getAnnotations() {
        return annotations;
    }

    public void addAnnotation(Annotation annotation) {
        this.annotations.add(annotation);
    }
    public List<TransformationDefinitionParameter> getTransformationdefinitionparameters() {
        return transformationdefinitionparameters;
    }

    public void addTransformationdefinitionparameter(Transformationdefinitionparameter transformationdefinitionparameter) {
        this.transformationdefinitionparameters.add(transformationdefinitionparameter);
    }
    public List<UseDeclaration> getUsedeclarations() {
        return usedeclarations;
    }

    public void addUsedeclaration(Usedeclaration usedeclaration) {
        this.usedeclarations.add(usedeclaration);
    }
    public List<TransformationDefinitionParameter> getTransformationdefinitionparameters() {
        return transformationdefinitionparameters;
    }

    public void addTransformationdefinitionparameter(Transformationdefinitionparameter transformationdefinitionparameter) {
        this.transformationdefinitionparameters.add(transformationdefinitionparameter);
    }

}