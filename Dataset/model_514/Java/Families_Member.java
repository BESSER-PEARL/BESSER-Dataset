





import java.util.List;
import java.util.ArrayList;

public class Families_Member extends uncertainty_ModelElement, uncertainty_aMember {

    private String firstName;
    private int age;





    private aMember amember;


    public Families_Member(
        String firstName,        int age    ) {
        super(
        );
        this.firstName = firstName;
        this.age = age;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public aMember getAmember() {
        return amember;
    }

    public void setAmember(aMember amember) {
        this.amember = amember;
    }

}