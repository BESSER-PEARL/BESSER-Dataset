





import java.util.List;
import java.util.ArrayList;

public class Families_FamilyMember extends uncertainty_aFamilyMember, uncertainty_ModelElement {

    private String name;



    public Families_FamilyMember(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}