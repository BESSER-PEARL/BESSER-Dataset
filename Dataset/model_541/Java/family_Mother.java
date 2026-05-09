





import java.util.List;
import java.util.ArrayList;

public class family_Mother  {

    private String Name;
    private int Age;





    private family_Father family_father;




    private family_FatherInLove family_fatherinlove;


    public family_Mother(
        String Name,        int Age    ) {
        this.Name = Name;
        this.Age = Age;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }

    public family_Father getFamily_father() {
        return family_father;
    }

    public void setFamily_father(family_Father family_father) {
        this.family_father = family_father;
    }
    public family_FatherInLove getFamily_fatherinlove() {
        return family_fatherinlove;
    }

    public void setFamily_fatherinlove(family_FatherInLove family_fatherinlove) {
        this.family_fatherinlove = family_fatherinlove;
    }

}