





import java.util.List;
import java.util.ArrayList;

public class Vendor2Adapter  {






    private List<Vendor2Sound> vendor2sounds;


    public Vendor2Adapter(
    ) {
        this.vendor2sounds = new ArrayList<>();
    }

    public Vendor2Adapter(
        ArrayList<Vendor2Sound> vendor2sounds    ) {
        this.vendor2sounds = vendor2sounds;
    }


    public List<Vendor2Sound> getVendor2sounds() {
        return vendor2sounds;
    }

    public void addVendor2sound(Vendor2sound vendor2sound) {
        this.vendor2sounds.add(vendor2sound);
    }

}