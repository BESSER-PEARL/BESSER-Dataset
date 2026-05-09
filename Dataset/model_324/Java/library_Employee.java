





import java.util.List;
import java.util.ArrayList;

public class library_Employee  {

    private int age;
    private String name;



    public library_Employee(
        int age,        String name    ) {
        this.age = age;
        this.name = name;
    }


    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}