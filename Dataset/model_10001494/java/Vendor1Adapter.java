





import java.util.List;
import java.util.ArrayList;

public class Vendor1Adapter  {






    private List<Vendor1Sound> vendor1sounds;


    public Vendor1Adapter(
    ) {
        this.vendor1sounds = new ArrayList<>();
    }

    public Vendor1Adapter(
        ArrayList<Vendor1Sound> vendor1sounds    ) {
        this.vendor1sounds = vendor1sounds;
    }


    public List<Vendor1Sound> getVendor1sounds() {
        return vendor1sounds;
    }

    public void addVendor1sound(Vendor1sound vendor1sound) {
        this.vendor1sounds.add(vendor1sound);
    }

}