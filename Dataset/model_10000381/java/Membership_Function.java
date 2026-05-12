





import java.util.List;
import java.util.ArrayList;

public class Membership_Function  {

    private float B;
    private float HasUID;
    private float A;
    private String HasName;



    public Membership_Function(
        float B,        float HasUID,        float A,        String HasName    ) {
        this.B = B;
        this.HasUID = HasUID;
        this.A = A;
        this.HasName = HasName;
    }


    public float getB() {
        return B;
    }

    public void setB(float B) {
        this.B = B;
    }
    public float getHasuid() {
        return HasUID;
    }

    public void setHasuid(float HasUID) {
        this.HasUID = HasUID;
    }
    public float getA() {
        return A;
    }

    public void setA(float A) {
        this.A = A;
    }
    public String getHasname() {
        return HasName;
    }

    public void setHasname(String HasName) {
        this.HasName = HasName;
    }


}