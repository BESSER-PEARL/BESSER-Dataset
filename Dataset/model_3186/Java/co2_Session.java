





import java.util.List;
import java.util.ArrayList;

public class co2_Session extends VariableDeclaration {






    private co2_TellAndReturn co2_tellandreturn;




    private co2_TellAndWait co2_tellandwait;




    private co2_ContractDefinition co2_contractdefinition;




    private co2_Contract co2_contract;


    public co2_Session(
    ) {
        super(
        );
    }



    public co2_TellAndReturn getCo2_tellandreturn() {
        return co2_tellandreturn;
    }

    public void setCo2_tellandreturn(co2_TellAndReturn co2_tellandreturn) {
        this.co2_tellandreturn = co2_tellandreturn;
    }
    public co2_TellAndWait getCo2_tellandwait() {
        return co2_tellandwait;
    }

    public void setCo2_tellandwait(co2_TellAndWait co2_tellandwait) {
        this.co2_tellandwait = co2_tellandwait;
    }
    public co2_ContractDefinition getCo2_contractdefinition() {
        return co2_contractdefinition;
    }

    public void setCo2_contractdefinition(co2_ContractDefinition co2_contractdefinition) {
        this.co2_contractdefinition = co2_contractdefinition;
    }
    public co2_Contract getCo2_contract() {
        return co2_contract;
    }

    public void setCo2_contract(co2_Contract co2_contract) {
        this.co2_contract = co2_contract;
    }

}