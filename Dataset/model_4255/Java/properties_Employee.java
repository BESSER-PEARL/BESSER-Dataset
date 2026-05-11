





import java.util.List;
import java.util.ArrayList;

public class properties_Employee extends Person {

    private int hasAge;
    private int hasSalary;



    public properties_Employee(
        int hasAge,        int hasSalary    ) {
        super(
        );
        this.hasAge = hasAge;
        this.hasSalary = hasSalary;
    }


    public int getHasage() {
        return hasAge;
    }

    public void setHasage(int hasAge) {
        this.hasAge = hasAge;
    }
    public int getHassalary() {
        return hasSalary;
    }

    public void setHassalary(int hasSalary) {
        this.hasSalary = hasSalary;
    }


}