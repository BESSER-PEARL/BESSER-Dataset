





import java.util.List;
import java.util.ArrayList;

public class ktest206_X  {






    private List<ktest206_W> ktest206_ws;


    public ktest206_X(
    ) {
        this.ktest206_ws = new ArrayList<>();
    }

    public ktest206_X(
        ArrayList<ktest206_W> ktest206_ws    ) {
        this.ktest206_ws = ktest206_ws;
    }


    public List<ktest206_W> getKtest206_ws() {
        return ktest206_ws;
    }

    public void addKtest206_w(Ktest206_w ktest206_w) {
        this.ktest206_ws.add(ktest206_w);
    }

}