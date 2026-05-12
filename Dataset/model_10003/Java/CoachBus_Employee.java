





import java.util.List;
import java.util.ArrayList;

public class CoachBus_Employee  {

    private int id;
    private float baseSalary;



    public CoachBus_Employee(
        int id,        float baseSalary    ) {
        this.id = id;
        this.baseSalary = baseSalary;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public float getBasesalary() {
        return baseSalary;
    }

    public void setBasesalary(float baseSalary) {
        this.baseSalary = baseSalary;
    }


}