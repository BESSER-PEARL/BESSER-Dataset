





import java.util.List;
import java.util.ArrayList;

public class oaam_library_ResourceBundle extends common_OaamBaseElementA, library_ResourceConsumerA {

    private float mass;
    private float mtbf;
    private float cost;



    public oaam_library_ResourceBundle(
        float mass,        float mtbf,        float cost    ) {
        super(
        );
        this.mass = mass;
        this.mtbf = mtbf;
        this.cost = cost;
    }


    public float getMass() {
        return mass;
    }

    public void setMass(float mass) {
        this.mass = mass;
    }
    public float getMtbf() {
        return mtbf;
    }

    public void setMtbf(float mtbf) {
        this.mtbf = mtbf;
    }
    public float getCost() {
        return cost;
    }

    public void setCost(float cost) {
        this.cost = cost;
    }


}