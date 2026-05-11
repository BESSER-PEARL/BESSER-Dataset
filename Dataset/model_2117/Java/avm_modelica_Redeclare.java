





import java.util.List;
import java.util.ArrayList;

public class avm_modelica_Redeclare extends DomainModelParameter {

    private String Type;
    private String Locator;



    public avm_modelica_Redeclare(
        String Type,        String Locator    ) {
        super(
        );
        this.Type = Type;
        this.Locator = Locator;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getLocator() {
        return Locator;
    }

    public void setLocator(String Locator) {
        this.Locator = Locator;
    }


}