





import java.util.List;
import java.util.ArrayList;

public class Oddelek2  {






    private List<Oseba4> oseba4s;


    public Oddelek2(
    ) {
        this.oseba4s = new ArrayList<>();
    }

    public Oddelek2(
        ArrayList<Oseba4> oseba4s    ) {
        this.oseba4s = oseba4s;
    }


    public List<Oseba4> getOseba4s() {
        return oseba4s;
    }

    public void addOseba4(Oseba4 oseba4) {
        this.oseba4s.add(oseba4);
    }

}