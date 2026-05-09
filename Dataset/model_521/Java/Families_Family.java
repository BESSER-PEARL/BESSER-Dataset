





import java.util.List;
import java.util.ArrayList;

public class Families_Family extends uncertainty_ModelElement, uncertainty_aFamily {

    private String name;



    public Families_Family(
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