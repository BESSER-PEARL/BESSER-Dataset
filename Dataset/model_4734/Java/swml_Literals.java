





import java.util.List;
import java.util.ArrayList;

public class swml_Literals  {

    private String name;





    private swml_Enumeration swml_enumeration;


    public swml_Literals(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public swml_Enumeration getSwml_enumeration() {
        return swml_enumeration;
    }

    public void setSwml_enumeration(swml_Enumeration swml_enumeration) {
        this.swml_enumeration = swml_enumeration;
    }

}