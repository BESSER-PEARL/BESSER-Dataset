





import java.util.List;
import java.util.ArrayList;

public class co2_Action  {

    private String name;





    private co2_Contract co2_contract;


    public co2_Action(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public co2_Contract getCo2_contract() {
        return co2_contract;
    }

    public void setCo2_contract(co2_Contract co2_contract) {
        this.co2_contract = co2_contract;
    }

}