





import java.util.List;
import java.util.ArrayList;

public class multiview4_E extends Named {






    private multiview4_A multiview4_a;




    private List<multiview4_F> multiview4_fs;


    public multiview4_E(
    ) {
        super(
        );
        this.multiview4_fs = new ArrayList<>();
    }

    public multiview4_E(
        ArrayList<multiview4_F> multiview4_fs    ) {
        this.multiview4_fs = multiview4_fs;
    }


    public multiview4_A getMultiview4_a() {
        return multiview4_a;
    }

    public void setMultiview4_a(multiview4_A multiview4_a) {
        this.multiview4_a = multiview4_a;
    }
    public List<multiview4_F> getMultiview4_fs() {
        return multiview4_fs;
    }

    public void addMultiview4_f(Multiview4_f multiview4_f) {
        this.multiview4_fs.add(multiview4_f);
    }

}