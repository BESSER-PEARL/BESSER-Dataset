





import java.util.List;
import java.util.ArrayList;

public class CoachBusWithEDataType_Employee  {

    private float baseSalary;
    private int id;



    public CoachBusWithEDataType_Employee(
        float baseSalary,        int id    ) {
        this.baseSalary = baseSalary;
        this.id = id;
    }


    public float getBasesalary() {
        return baseSalary;
    }

    public void setBasesalary(float baseSalary) {
        this.baseSalary = baseSalary;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}