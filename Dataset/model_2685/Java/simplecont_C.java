





import java.util.List;
import java.util.ArrayList;

public class simplecont_C  {

    private String id;





    private simplecont_B simplecont_b;




    private simplecont_A simplecont_a;


    public simplecont_C(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public simplecont_B getSimplecont_b() {
        return simplecont_b;
    }

    public void setSimplecont_b(simplecont_B simplecont_b) {
        this.simplecont_b = simplecont_b;
    }
    public simplecont_A getSimplecont_a() {
        return simplecont_a;
    }

    public void setSimplecont_a(simplecont_A simplecont_a) {
        this.simplecont_a = simplecont_a;
    }

}