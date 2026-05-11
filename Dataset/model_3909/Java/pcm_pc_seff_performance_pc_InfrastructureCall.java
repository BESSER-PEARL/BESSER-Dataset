





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_seff_performance_pc_InfrastructureCall extends CallAction {






    private InfrastructureSignature infrastructuresignature;




    private PCMRandomVariable pcmrandomvariable;




    private InfrastructureRequiredRole infrastructurerequiredrole;


    public pcm_pc_seff_performance_pc_InfrastructureCall(
    ) {
        super(
        );
    }



    public InfrastructureSignature getInfrastructuresignature() {
        return infrastructuresignature;
    }

    public void setInfrastructuresignature(InfrastructureSignature infrastructuresignature) {
        this.infrastructuresignature = infrastructuresignature;
    }
    public PCMRandomVariable getPcmrandomvariable() {
        return pcmrandomvariable;
    }

    public void setPcmrandomvariable(PCMRandomVariable pcmrandomvariable) {
        this.pcmrandomvariable = pcmrandomvariable;
    }
    public InfrastructureRequiredRole getInfrastructurerequiredrole() {
        return infrastructurerequiredrole;
    }

    public void setInfrastructurerequiredrole(InfrastructureRequiredRole infrastructurerequiredrole) {
        this.infrastructurerequiredrole = infrastructurerequiredrole;
    }

}