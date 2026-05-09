





import java.util.List;
import java.util.ArrayList;

public class family_university  {

    private String name;





    private family_Root family_root;


    public family_university(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public family_Root getFamily_root() {
        return family_root;
    }

    public void setFamily_root(family_Root family_root) {
        this.family_root = family_root;
    }

}