





import java.util.List;
import java.util.ArrayList;

public class family_Person extends FNamedElement {

    private String sex;
    private int age;



    public family_Person(
        String sex,        int age    ) {
        super(
        );
        this.sex = sex;
        this.age = age;
    }


    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }


}