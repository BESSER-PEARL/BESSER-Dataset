





import java.util.List;
import java.util.ArrayList;

public class pcm_av_seff_performance_av_InfrastructureCall extends CallAction {






    private InfrastructureSignature infrastructuresignature;




    private InfrastructureRequiredRole infrastructurerequiredrole;




    private PCMRandomVariable pcmrandomvariable;


    public pcm_av_seff_performance_av_InfrastructureCall(
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
    public InfrastructureRequiredRole getInfrastructurerequiredrole() {
        return infrastructurerequiredrole;
    }

    public void setInfrastructurerequiredrole(InfrastructureRequiredRole infrastructurerequiredrole) {
        this.infrastructurerequiredrole = infrastructurerequiredrole;
    }
    public PCMRandomVariable getPcmrandomvariable() {
        return pcmrandomvariable;
    }

    public void setPcmrandomvariable(PCMRandomVariable pcmrandomvariable) {
        this.pcmrandomvariable = pcmrandomvariable;
    }

}