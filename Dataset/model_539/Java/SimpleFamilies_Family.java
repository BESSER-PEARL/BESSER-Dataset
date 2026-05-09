





import java.util.List;
import java.util.ArrayList;

public class SimpleFamilies_Family  {

    private String name;





    private SimpleFamilies_FamilyRegister simplefamilies_familyregister;


    public SimpleFamilies_Family(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SimpleFamilies_FamilyRegister getSimplefamilies_familyregister() {
        return simplefamilies_familyregister;
    }

    public void setSimplefamilies_familyregister(SimpleFamilies_FamilyRegister simplefamilies_familyregister) {
        this.simplefamilies_familyregister = simplefamilies_familyregister;
    }

}