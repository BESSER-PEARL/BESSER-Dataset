





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwComputing_HwPLD extends HwComputingResource {

    private String ndLUT_Inputs;
    private String technology;
    private String nbFlipFlops;
    private String organization;
    private String nbLUTs;



    public MARTE_HwComputing_HwPLD(
        String ndLUT_Inputs,        String technology,        String nbFlipFlops,        String organization,        String nbLUTs    ) {
        super(
        );
        this.ndLUT_Inputs = ndLUT_Inputs;
        this.technology = technology;
        this.nbFlipFlops = nbFlipFlops;
        this.organization = organization;
        this.nbLUTs = nbLUTs;
    }


    public String getNdlut_inputs() {
        return ndLUT_Inputs;
    }

    public void setNdlut_inputs(String ndLUT_Inputs) {
        this.ndLUT_Inputs = ndLUT_Inputs;
    }
    public String getTechnology() {
        return technology;
    }

    public void setTechnology(String technology) {
        this.technology = technology;
    }
    public String getNbflipflops() {
        return nbFlipFlops;
    }

    public void setNbflipflops(String nbFlipFlops) {
        this.nbFlipFlops = nbFlipFlops;
    }
    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
    }
    public String getNbluts() {
        return nbLUTs;
    }

    public void setNbluts(String nbLUTs) {
        this.nbLUTs = nbLUTs;
    }


}