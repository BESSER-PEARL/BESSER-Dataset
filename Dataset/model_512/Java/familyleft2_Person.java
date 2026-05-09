





import java.util.List;
import java.util.ArrayList;

public class familyleft2_Person  {

    private String name;
    private boolean isMale;
    private int age;



    public familyleft2_Person(
        String name,        boolean isMale,        int age    ) {
        this.name = name;
        this.isMale = isMale;
        this.age = age;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsmale() {
        return isMale;
    }

    public void setIsmale(boolean isMale) {
        this.isMale = isMale;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }


}