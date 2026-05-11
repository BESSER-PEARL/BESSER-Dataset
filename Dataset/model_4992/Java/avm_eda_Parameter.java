





import java.util.List;
import java.util.ArrayList;

public class avm_eda_Parameter extends DomainModelParameter {

    private String Locator;



    public avm_eda_Parameter(
        String Locator    ) {
        super(
        );
        this.Locator = Locator;
    }


    public String getLocator() {
        return Locator;
    }

    public void setLocator(String Locator) {
        this.Locator = Locator;
    }


}