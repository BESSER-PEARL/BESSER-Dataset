





import java.util.List;
import java.util.ArrayList;

public class library_Employee  {

    private String name;
    private int age;



    public library_Employee(
        String name,        int age    ) {
        this.name = name;
        this.age = age;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }


}