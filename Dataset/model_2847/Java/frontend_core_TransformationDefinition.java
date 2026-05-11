





import java.util.List;
import java.util.ArrayList;

public class frontend_core_TransformationDefinition extends ModuleDefinition {






    private List<TransformationDefinitionParameter> transformationdefinitionparameters;




    private List<TransformationDefinitionParameter> transformationdefinitionparameters;




    private List<UseDeclaration> usedeclarations;


    public frontend_core_TransformationDefinition(
    ) {
        super(
        );
        this.transformationdefinitionparameters = new ArrayList<>();
        this.transformationdefinitionparameters = new ArrayList<>();
        this.usedeclarations = new ArrayList<>();
    }

    public frontend_core_TransformationDefinition(
        ArrayList<TransformationDefinitionParameter> transformationdefinitionparameters,        ArrayList<TransformationDefinitionParameter> transformationdefinitionparameters,        ArrayList<UseDeclaration> usedeclarations    ) {
        this.transformationdefinitionparameters = transformationdefinitionparameters;
        this.transformationdefinitionparameters = transformationdefinitionparameters;
        this.usedeclarations = usedeclarations;
    }


    public List<TransformationDefinitionParameter> getTransformationdefinitionparameters() {
        return transformationdefinitionparameters;
    }

    public void addTransformationdefinitionparameter(Transformationdefinitionparameter transformationdefinitionparameter) {
        this.transformationdefinitionparameters.add(transformationdefinitionparameter);
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

}