





import java.util.List;
import java.util.ArrayList;

public class co2_ProcessDefinition  {

    private boolean withoutRestrictions;
    private String name;





    private co2_ProcessCall co2_processcall;




    private co2_ContractsAndProcessesDeclaration co2_contractsandprocessesdeclaration;




    private co2_HonestyDeclaration co2_honestydeclaration;




    private co2_ParallelProcesses co2_parallelprocesses;


    public co2_ProcessDefinition(
        boolean withoutRestrictions,        String name    ) {
        this.withoutRestrictions = withoutRestrictions;
        this.name = name;
    }


    public boolean getWithoutrestrictions() {
        return withoutRestrictions;
    }

    public void setWithoutrestrictions(boolean withoutRestrictions) {
        this.withoutRestrictions = withoutRestrictions;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public co2_ProcessCall getCo2_processcall() {
        return co2_processcall;
    }

    public void setCo2_processcall(co2_ProcessCall co2_processcall) {
        this.co2_processcall = co2_processcall;
    }
    public co2_ContractsAndProcessesDeclaration getCo2_contractsandprocessesdeclaration() {
        return co2_contractsandprocessesdeclaration;
    }

    public void setCo2_contractsandprocessesdeclaration(co2_ContractsAndProcessesDeclaration co2_contractsandprocessesdeclaration) {
        this.co2_contractsandprocessesdeclaration = co2_contractsandprocessesdeclaration;
    }
    public co2_HonestyDeclaration getCo2_honestydeclaration() {
        return co2_honestydeclaration;
    }

    public void setCo2_honestydeclaration(co2_HonestyDeclaration co2_honestydeclaration) {
        this.co2_honestydeclaration = co2_honestydeclaration;
    }
    public co2_ParallelProcesses getCo2_parallelprocesses() {
        return co2_parallelprocesses;
    }

    public void setCo2_parallelprocesses(co2_ParallelProcesses co2_parallelprocesses) {
        this.co2_parallelprocesses = co2_parallelprocesses;
    }

}