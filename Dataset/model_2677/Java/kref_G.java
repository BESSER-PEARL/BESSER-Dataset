





import java.util.List;
import java.util.ArrayList;

public class kref_G extends Named {






    private kref_B kref_b;




    private List<kref_H> kref_hs;


    public kref_G(
    ) {
        super(
        );
        this.kref_hs = new ArrayList<>();
    }

    public kref_G(
        ArrayList<kref_H> kref_hs    ) {
        this.kref_hs = kref_hs;
    }


    public kref_B getKref_b() {
        return kref_b;
    }

    public void setKref_b(kref_B kref_b) {
        this.kref_b = kref_b;
    }
    public List<kref_H> getKref_hs() {
        return kref_hs;
    }

    public void addKref_h(Kref_h kref_h) {
        this.kref_hs.add(kref_h);
    }

}