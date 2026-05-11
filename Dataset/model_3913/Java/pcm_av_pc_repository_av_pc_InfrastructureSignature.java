





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_repository_av_pc_InfrastructureSignature extends Signature {






    private List<Parameter> parameters;


    public pcm_av_pc_repository_av_pc_InfrastructureSignature(
    ) {
        super(
        );
        this.parameters = new ArrayList<>();
    }

    public pcm_av_pc_repository_av_pc_InfrastructureSignature(
        ArrayList<Parameter> parameters    ) {
        this.parameters = parameters;
    }


    public List<Parameter> getParameters() {
        return parameters;
    }

    public void addParameter(Parameter parameter) {
        this.parameters.add(parameter);
    }

}