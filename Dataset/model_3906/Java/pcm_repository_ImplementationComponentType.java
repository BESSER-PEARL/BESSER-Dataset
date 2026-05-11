





import java.util.List;
import java.util.ArrayList;

public class pcm_repository_ImplementationComponentType extends CompleteComponentType {






    private List<VariableUsage> variableusages;


    public pcm_repository_ImplementationComponentType(
    ) {
        super(
        );
        this.variableusages = new ArrayList<>();
    }

    public pcm_repository_ImplementationComponentType(
        ArrayList<VariableUsage> variableusages    ) {
        this.variableusages = variableusages;
    }


    public List<VariableUsage> getVariableusages() {
        return variableusages;
    }

    public void addVariableusage(Variableusage variableusage) {
        this.variableusages.add(variableusage);
    }

}