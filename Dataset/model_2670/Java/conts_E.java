





import java.util.List;
import java.util.ArrayList;

public class conts_E extends B, Named {






    private List<conts_F> conts_fs;


    public conts_E(
    ) {
        super(
        );
        this.conts_fs = new ArrayList<>();
    }

    public conts_E(
        ArrayList<conts_F> conts_fs    ) {
        this.conts_fs = conts_fs;
    }


    public List<conts_F> getConts_fs() {
        return conts_fs;
    }

    public void addConts_f(Conts_f conts_f) {
        this.conts_fs.add(conts_f);
    }

}