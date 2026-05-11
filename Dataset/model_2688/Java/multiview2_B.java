





import java.util.List;
import java.util.ArrayList;

public class multiview2_B extends Named {






    private List<multiview2_C> multiview2_cs;




    private multiview2_A multiview2_a;


    public multiview2_B(
    ) {
        super(
        );
        this.multiview2_cs = new ArrayList<>();
    }

    public multiview2_B(
        ArrayList<multiview2_C> multiview2_cs    ) {
        this.multiview2_cs = multiview2_cs;
    }


    public List<multiview2_C> getMultiview2_cs() {
        return multiview2_cs;
    }

    public void addMultiview2_c(Multiview2_c multiview2_c) {
        this.multiview2_cs.add(multiview2_c);
    }
    public multiview2_A getMultiview2_a() {
        return multiview2_a;
    }

    public void setMultiview2_a(multiview2_A multiview2_a) {
        this.multiview2_a = multiview2_a;
    }

}