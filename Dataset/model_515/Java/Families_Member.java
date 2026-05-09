





import java.util.List;
import java.util.ArrayList;

public class Families_Member extends uncertainty_aMember, uncertainty_ModelElement {

    private int age;
    private String firstName;



    public Families_Member(
        int age,        String firstName    ) {
        super(
        );
        this.age = age;
        this.firstName = firstName;
    }


    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }


}