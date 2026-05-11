





import java.util.List;
import java.util.ArrayList;

public class avm_manufacturing_Parameter extends DomainModelParameter {

    private String Locator;
    private String Name;



    public avm_manufacturing_Parameter(
        String Locator,        String Name    ) {
        super(
        );
        this.Locator = Locator;
        this.Name = Name;
    }


    public String getLocator() {
        return Locator;
    }

    public void setLocator(String Locator) {
        this.Locator = Locator;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}