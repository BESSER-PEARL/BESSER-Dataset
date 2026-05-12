





import java.util.List;
import java.util.ArrayList;

public class customer  {

    private String address;
    private int age;
    private String name;
    private String source;



    public customer(
        String address,        int age,        String name,        String source    ) {
        this.address = address;
        this.age = age;
        this.name = name;
        this.source = source;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
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
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }


}