





import java.util.List;
import java.util.ArrayList;

public class seller  {

    private String section_name;
    private int number;
    private int salary;
    private String name;





    private section section;


    public seller(
        String section_name,        int number,        int salary,        String name    ) {
        this.section_name = section_name;
        this.number = number;
        this.salary = salary;
        this.name = name;
    }


    public String getSection_name() {
        return section_name;
    }

    public void setSection_name(String section_name) {
        this.section_name = section_name;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public section getSection() {
        return section;
    }

    public void setSection(section section) {
        this.section = section;
    }

}