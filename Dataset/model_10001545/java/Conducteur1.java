





import java.util.List;
import java.util.ArrayList;

public class Conducteur1  {






    private List<V_hicule1> v_hicule1s;




    private List<Trajet2> trajet2s;


    public Conducteur1(
    ) {
        this.v_hicule1s = new ArrayList<>();
        this.trajet2s = new ArrayList<>();
    }

    public Conducteur1(
        ArrayList<V_hicule1> v_hicule1s,        ArrayList<Trajet2> trajet2s    ) {
        this.v_hicule1s = v_hicule1s;
        this.trajet2s = trajet2s;
    }


    public List<V_hicule1> getV_hicule1s() {
        return v_hicule1s;
    }

    public void addV_hicule1(V_hicule1 v_hicule1) {
        this.v_hicule1s.add(v_hicule1);
    }
    public List<Trajet2> getTrajet2s() {
        return trajet2s;
    }

    public void addTrajet2(Trajet2 trajet2) {
        this.trajet2s.add(trajet2);
    }

}