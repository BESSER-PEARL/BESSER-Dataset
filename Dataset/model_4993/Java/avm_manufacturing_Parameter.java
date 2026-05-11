





import java.util.List;
import java.util.ArrayList;

public class avm_manufacturing_Parameter extends DomainModelParameter {

    private String Name;
    private String Locator;



    public avm_manufacturing_Parameter(
        String Name,        String Locator    ) {
        super(
        );
        this.Name = Name;
        this.Locator = Locator;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getLocator() {
        return Locator;
    }

    public void setLocator(String Locator) {
        this.Locator = Locator;
    }


}