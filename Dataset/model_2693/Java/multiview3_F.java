





import java.util.List;
import java.util.ArrayList;

public class multiview3_F extends Named {






    private List<multiview3_M> multiview3_ms;


    public multiview3_F(
    ) {
        super(
        );
        this.multiview3_ms = new ArrayList<>();
    }

    public multiview3_F(
        ArrayList<multiview3_M> multiview3_ms    ) {
        this.multiview3_ms = multiview3_ms;
    }


    public List<multiview3_M> getMultiview3_ms() {
        return multiview3_ms;
    }

    public void addMultiview3_m(Multiview3_m multiview3_m) {
        this.multiview3_ms.add(multiview3_m);
    }

}