





import java.util.List;
import java.util.ArrayList;

public class model2_B  {

    private int attB;





    private List<model2_C> model2_cs;




    private model2_A model2_a;


    public model2_B(
        int attB    ) {
        this.attB = attB;
        this.model2_cs = new ArrayList<>();
    }

    public model2_B(
        int attB        ArrayList<model2_C> model2_cs    ) {
        this.attB = attB;
        this.model2_cs = model2_cs;
    }

    public int getAttb() {
        return attB;
    }

    public void setAttb(int attB) {
        this.attB = attB;
    }

    public List<model2_C> getModel2_cs() {
        return model2_cs;
    }

    public void addModel2_c(Model2_c model2_c) {
        this.model2_cs.add(model2_c);
    }
    public model2_A getModel2_a() {
        return model2_a;
    }

    public void setModel2_a(model2_A model2_a) {
        this.model2_a = model2_a;
    }

}