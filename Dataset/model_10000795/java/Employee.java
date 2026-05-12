





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String position;
    private String name;
    private int yearsHere;
    private int salary;



    public Employee(
        String position,        String name,        int yearsHere,        int salary    ) {
        this.position = position;
        this.name = name;
        this.yearsHere = yearsHere;
        this.salary = salary;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getYearshere() {
        return yearsHere;
    }

    public void setYearshere(int yearsHere) {
        this.yearsHere = yearsHere;
    }
    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }


}