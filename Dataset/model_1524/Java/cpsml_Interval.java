





import java.util.List;
import java.util.ArrayList;

public class cpsml_Interval  {

    private float subinterval;
    private float right;
    private String name;
    private float left;





    private cpsml_ODE cpsml_ode;


    public cpsml_Interval(
        float subinterval,        float right,        String name,        float left    ) {
        this.subinterval = subinterval;
        this.right = right;
        this.name = name;
        this.left = left;
    }


    public float getSubinterval() {
        return subinterval;
    }

    public void setSubinterval(float subinterval) {
        this.subinterval = subinterval;
    }
    public float getRight() {
        return right;
    }

    public void setRight(float right) {
        this.right = right;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getLeft() {
        return left;
    }

    public void setLeft(float left) {
        this.left = left;
    }

    public cpsml_ODE getCpsml_ode() {
        return cpsml_ode;
    }

    public void setCpsml_ode(cpsml_ODE cpsml_ode) {
        this.cpsml_ode = cpsml_ode;
    }

}