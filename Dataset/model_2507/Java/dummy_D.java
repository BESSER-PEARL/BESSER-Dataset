





import java.util.List;
import java.util.ArrayList;

public class dummy_D  {

    private String name;
    private float l;
    private float m;





    private dummy_A dummy_a;


    public dummy_D(
        String name,        float l,        float m    ) {
        this.name = name;
        this.l = l;
        this.m = m;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getL() {
        return l;
    }

    public void setL(float l) {
        this.l = l;
    }
    public float getM() {
        return m;
    }

    public void setM(float m) {
        this.m = m;
    }

    public dummy_A getDummy_a() {
        return dummy_a;
    }

    public void setDummy_a(dummy_A dummy_a) {
        this.dummy_a = dummy_a;
    }

}