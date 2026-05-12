





import java.util.List;
import java.util.ArrayList;

public class Vendor2Sound  {






    private List<Vendor2Adapter> vendor2adapters;


    public Vendor2Sound(
    ) {
        this.vendor2adapters = new ArrayList<>();
    }

    public Vendor2Sound(
        ArrayList<Vendor2Adapter> vendor2adapters    ) {
        this.vendor2adapters = vendor2adapters;
    }


    public List<Vendor2Adapter> getVendor2adapters() {
        return vendor2adapters;
    }

    public void addVendor2adapter(Vendor2adapter vendor2adapter) {
        this.vendor2adapters.add(vendor2adapter);
    }

}