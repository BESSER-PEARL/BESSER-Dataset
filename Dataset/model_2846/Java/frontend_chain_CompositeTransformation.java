





import java.util.List;
import java.util.ArrayList;

public class frontend_chain_CompositeTransformation extends core_TransformationDefinition, chain_AvailableTransformation {






    private List<TransformationExecution> transformationexecutions;


    public frontend_chain_CompositeTransformation(
    ) {
        super(
        );
        this.transformationexecutions = new ArrayList<>();
    }

    public frontend_chain_CompositeTransformation(
        ArrayList<TransformationExecution> transformationexecutions    ) {
        this.transformationexecutions = transformationexecutions;
    }


    public List<TransformationExecution> getTransformationexecutions() {
        return transformationexecutions;
    }

    public void addTransformationexecution(Transformationexecution transformationexecution) {
        this.transformationexecutions.add(transformationexecution);
    }

}