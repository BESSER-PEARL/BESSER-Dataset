





import java.util.List;
import java.util.ArrayList;

public class multiview2_E extends Named {






    private multiview2_A multiview2_a;




    private List<multiview2_F> multiview2_fs;


    public multiview2_E(
    ) {
        super(
        );
        this.multiview2_fs = new ArrayList<>();
    }

    public multiview2_E(
        ArrayList<multiview2_F> multiview2_fs    ) {
        this.multiview2_fs = multiview2_fs;
    }


    public multiview2_A getMultiview2_a() {
        return multiview2_a;
    }

    public void setMultiview2_a(multiview2_A multiview2_a) {
        this.multiview2_a = multiview2_a;
    }
    public List<multiview2_F> getMultiview2_fs() {
        return multiview2_fs;
    }

    public void addMultiview2_f(Multiview2_f multiview2_f) {
        this.multiview2_fs.add(multiview2_f);
    }

}