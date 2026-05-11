





import java.util.List;
import java.util.ArrayList;

public class p2_Repository  {






    private List<p2_Property> p2_propertys;


    public p2_Repository(
    ) {
        this.p2_propertys = new ArrayList<>();
    }

    public p2_Repository(
        ArrayList<p2_Property> p2_propertys    ) {
        this.p2_propertys = p2_propertys;
    }


    public List<p2_Property> getP2_propertys() {
        return p2_propertys;
    }

    public void addP2_property(P2_property p2_property) {
        this.p2_propertys.add(p2_property);
    }

}