





import java.util.List;
import java.util.ArrayList;

public class Teacher  {

    private int Phone;
    private String name;
    private int Age;



    public Teacher(
        int Phone,        String name,        int Age    ) {
        this.Phone = Phone;
        this.name = name;
        this.Age = Age;
    }


    public int getPhone() {
        return Phone;
    }

    public void setPhone(int Phone) {
        this.Phone = Phone;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }


}