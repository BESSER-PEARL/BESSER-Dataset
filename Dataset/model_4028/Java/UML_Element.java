





import java.util.List;
import java.util.ArrayList;

public class UML_Element  {

    private String visibility;
    private String name;



    public UML_Element(
        String visibility,        String name    ) {
        this.visibility = visibility;
        this.name = name;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}