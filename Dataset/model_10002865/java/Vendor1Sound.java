





import java.util.List;
import java.util.ArrayList;

public class Vendor1Sound  {






    private List<Vendor1Adapter> vendor1adapters;


    public Vendor1Sound(
    ) {
        this.vendor1adapters = new ArrayList<>();
    }

    public Vendor1Sound(
        ArrayList<Vendor1Adapter> vendor1adapters    ) {
        this.vendor1adapters = vendor1adapters;
    }


    public List<Vendor1Adapter> getVendor1adapters() {
        return vendor1adapters;
    }

    public void addVendor1adapter(Vendor1adapter vendor1adapter) {
        this.vendor1adapters.add(vendor1adapter);
    }

}