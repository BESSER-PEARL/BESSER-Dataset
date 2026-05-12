





import java.util.List;
import java.util.ArrayList;

public class Conducteur  {






    private List<V_hicule> v_hicules;




    private List<Trajet1> trajet1s;


    public Conducteur(
    ) {
        this.v_hicules = new ArrayList<>();
        this.trajet1s = new ArrayList<>();
    }

    public Conducteur(
        ArrayList<V_hicule> v_hicules,        ArrayList<Trajet1> trajet1s    ) {
        this.v_hicules = v_hicules;
        this.trajet1s = trajet1s;
    }


    public List<V_hicule> getV_hicules() {
        return v_hicules;
    }

    public void addV_hicule(V_hicule v_hicule) {
        this.v_hicules.add(v_hicule);
    }
    public List<Trajet1> getTrajet1s() {
        return trajet1s;
    }

    public void addTrajet1(Trajet1 trajet1) {
        this.trajet1s.add(trajet1);
    }

}