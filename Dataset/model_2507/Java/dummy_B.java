





import java.util.List;
import java.util.ArrayList;

public class dummy_B  {

    private float z;
    private float y;





    private dummy_A dummy_a;




    private dummy_C dummy_c;


    public dummy_B(
        float z,        float y    ) {
        this.z = z;
        this.y = y;
    }


    public float getZ() {
        return z;
    }

    public void setZ(float z) {
        this.z = z;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }

    public dummy_A getDummy_a() {
        return dummy_a;
    }

    public void setDummy_a(dummy_A dummy_a) {
        this.dummy_a = dummy_a;
    }
    public dummy_C getDummy_c() {
        return dummy_c;
    }

    public void setDummy_c(dummy_C dummy_c) {
        this.dummy_c = dummy_c;
    }

}