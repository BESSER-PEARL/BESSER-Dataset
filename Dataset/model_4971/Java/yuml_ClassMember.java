





import java.util.List;
import java.util.ArrayList;

public class yuml_ClassMember  {

    private String name;
    private String visibility;



    public yuml_ClassMember(
        String name,        String visibility    ) {
        this.name = name;
        this.visibility = visibility;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }


}