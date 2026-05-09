





import java.util.List;
import java.util.ArrayList;

public class family_Daughter  {

    private int Age;
    private String Name;





    private family_Father family_father;


    public family_Daughter(
        int Age,        String Name    ) {
        this.Age = Age;
        this.Name = Name;
    }


    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public family_Father getFamily_father() {
        return family_father;
    }

    public void setFamily_father(family_Father family_father) {
        this.family_father = family_father;
    }

}