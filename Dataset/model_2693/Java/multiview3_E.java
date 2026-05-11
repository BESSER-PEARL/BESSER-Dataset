





import java.util.List;
import java.util.ArrayList;

public class multiview3_E extends Named {






    private List<multiview3_F> multiview3_fs;




    private multiview3_A multiview3_a;




    private List<multiview3_W> multiview3_ws;


    public multiview3_E(
    ) {
        super(
        );
        this.multiview3_fs = new ArrayList<>();
        this.multiview3_ws = new ArrayList<>();
    }

    public multiview3_E(
        ArrayList<multiview3_F> multiview3_fs,        ArrayList<multiview3_W> multiview3_ws    ) {
        this.multiview3_fs = multiview3_fs;
        this.multiview3_ws = multiview3_ws;
    }


    public List<multiview3_F> getMultiview3_fs() {
        return multiview3_fs;
    }

    public void addMultiview3_f(Multiview3_f multiview3_f) {
        this.multiview3_fs.add(multiview3_f);
    }
    public multiview3_A getMultiview3_a() {
        return multiview3_a;
    }

    public void setMultiview3_a(multiview3_A multiview3_a) {
        this.multiview3_a = multiview3_a;
    }
    public List<multiview3_W> getMultiview3_ws() {
        return multiview3_ws;
    }

    public void addMultiview3_w(Multiview3_w multiview3_w) {
        this.multiview3_ws.add(multiview3_w);
    }

}