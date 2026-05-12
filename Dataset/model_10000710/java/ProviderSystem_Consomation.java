





import java.util.List;
import java.util.ArrayList;

public class ProviderSystem_Consomation  {

    private int pricePerUnit;
    private String name;



    public ProviderSystem_Consomation(
        int pricePerUnit,        String name    ) {
        this.pricePerUnit = pricePerUnit;
        this.name = name;
    }


    public int getPriceperunit() {
        return pricePerUnit;
    }

    public void setPriceperunit(int pricePerUnit) {
        this.pricePerUnit = pricePerUnit;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}