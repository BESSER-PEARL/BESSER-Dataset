





import java.util.List;
import java.util.ArrayList;

public class co2_ContractDefinition  {

    private String name;





    private co2_ContractsAndProcessesDeclaration co2_contractsandprocessesdeclaration;


    public co2_ContractDefinition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public co2_ContractsAndProcessesDeclaration getCo2_contractsandprocessesdeclaration() {
        return co2_contractsandprocessesdeclaration;
    }

    public void setCo2_contractsandprocessesdeclaration(co2_ContractsAndProcessesDeclaration co2_contractsandprocessesdeclaration) {
        this.co2_contractsandprocessesdeclaration = co2_contractsandprocessesdeclaration;
    }

}