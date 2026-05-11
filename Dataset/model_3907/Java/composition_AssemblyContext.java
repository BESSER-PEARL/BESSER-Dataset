





import java.util.List;
import java.util.ArrayList;

public class composition_AssemblyContext  {






    private pcm_composition_ProvidedDelegationConnector pcm_composition_provideddelegationconnector;




    private pcm_performance_ComponentSpecifiedExecutionTime pcm_performance_componentspecifiedexecutiontime;




    private pcm_allocation_AllocationContext pcm_allocation_allocationcontext;




    private pcm_composition_ComposedStructure pcm_composition_composedstructure;




    private pcm_composition_RequiredDelegationConnector pcm_composition_requireddelegationconnector;




    private pcm_usagemodel_UserData pcm_usagemodel_userdata;


    public composition_AssemblyContext(
    ) {
    }



    public pcm_composition_ProvidedDelegationConnector getPcm_composition_provideddelegationconnector() {
        return pcm_composition_provideddelegationconnector;
    }

    public void setPcm_composition_provideddelegationconnector(pcm_composition_ProvidedDelegationConnector pcm_composition_provideddelegationconnector) {
        this.pcm_composition_provideddelegationconnector = pcm_composition_provideddelegationconnector;
    }
    public pcm_performance_ComponentSpecifiedExecutionTime getPcm_performance_componentspecifiedexecutiontime() {
        return pcm_performance_componentspecifiedexecutiontime;
    }

    public void setPcm_performance_componentspecifiedexecutiontime(pcm_performance_ComponentSpecifiedExecutionTime pcm_performance_componentspecifiedexecutiontime) {
        this.pcm_performance_componentspecifiedexecutiontime = pcm_performance_componentspecifiedexecutiontime;
    }
    public pcm_allocation_AllocationContext getPcm_allocation_allocationcontext() {
        return pcm_allocation_allocationcontext;
    }

    public void setPcm_allocation_allocationcontext(pcm_allocation_AllocationContext pcm_allocation_allocationcontext) {
        this.pcm_allocation_allocationcontext = pcm_allocation_allocationcontext;
    }
    public pcm_composition_ComposedStructure getPcm_composition_composedstructure() {
        return pcm_composition_composedstructure;
    }

    public void setPcm_composition_composedstructure(pcm_composition_ComposedStructure pcm_composition_composedstructure) {
        this.pcm_composition_composedstructure = pcm_composition_composedstructure;
    }
    public pcm_composition_RequiredDelegationConnector getPcm_composition_requireddelegationconnector() {
        return pcm_composition_requireddelegationconnector;
    }

    public void setPcm_composition_requireddelegationconnector(pcm_composition_RequiredDelegationConnector pcm_composition_requireddelegationconnector) {
        this.pcm_composition_requireddelegationconnector = pcm_composition_requireddelegationconnector;
    }
    public pcm_usagemodel_UserData getPcm_usagemodel_userdata() {
        return pcm_usagemodel_userdata;
    }

    public void setPcm_usagemodel_userdata(pcm_usagemodel_UserData pcm_usagemodel_userdata) {
        this.pcm_usagemodel_userdata = pcm_usagemodel_userdata;
    }

}