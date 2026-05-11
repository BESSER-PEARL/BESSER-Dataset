





import java.util.List;
import java.util.ArrayList;

public class composition_AssemblyContext  {






    private pcm_composition_ComposedStructure pcm_composition_composedstructure;




    private pcm_allocation_AllocationContext pcm_allocation_allocationcontext;




    private pcm_composition_ProvidedDelegationConnector pcm_composition_provideddelegationconnector;




    private pcm_composition_RequiredDelegationConnector pcm_composition_requireddelegationconnector;


    public composition_AssemblyContext(
    ) {
    }



    public pcm_composition_ComposedStructure getPcm_composition_composedstructure() {
        return pcm_composition_composedstructure;
    }

    public void setPcm_composition_composedstructure(pcm_composition_ComposedStructure pcm_composition_composedstructure) {
        this.pcm_composition_composedstructure = pcm_composition_composedstructure;
    }
    public pcm_allocation_AllocationContext getPcm_allocation_allocationcontext() {
        return pcm_allocation_allocationcontext;
    }

    public void setPcm_allocation_allocationcontext(pcm_allocation_AllocationContext pcm_allocation_allocationcontext) {
        this.pcm_allocation_allocationcontext = pcm_allocation_allocationcontext;
    }
    public pcm_composition_ProvidedDelegationConnector getPcm_composition_provideddelegationconnector() {
        return pcm_composition_provideddelegationconnector;
    }

    public void setPcm_composition_provideddelegationconnector(pcm_composition_ProvidedDelegationConnector pcm_composition_provideddelegationconnector) {
        this.pcm_composition_provideddelegationconnector = pcm_composition_provideddelegationconnector;
    }
    public pcm_composition_RequiredDelegationConnector getPcm_composition_requireddelegationconnector() {
        return pcm_composition_requireddelegationconnector;
    }

    public void setPcm_composition_requireddelegationconnector(pcm_composition_RequiredDelegationConnector pcm_composition_requireddelegationconnector) {
        this.pcm_composition_requireddelegationconnector = pcm_composition_requireddelegationconnector;
    }

}