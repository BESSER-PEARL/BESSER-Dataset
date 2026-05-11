





import java.util.List;
import java.util.ArrayList;

public class kref_E extends Named, B {






    private List<kref_F> kref_fs;


    public kref_E(
    ) {
        super(
        );
        this.kref_fs = new ArrayList<>();
    }

    public kref_E(
        ArrayList<kref_F> kref_fs    ) {
        this.kref_fs = kref_fs;
    }


    public List<kref_F> getKref_fs() {
        return kref_fs;
    }

    public void addKref_f(Kref_f kref_f) {
        this.kref_fs.add(kref_f);
    }

}