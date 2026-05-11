





import java.util.List;
import java.util.ArrayList;

public class attributes_R  {

    private String name;





    private attributes_A attributes_a;


    public attributes_R(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public attributes_A getAttributes_a() {
        return attributes_a;
    }

    public void setAttributes_a(attributes_A attributes_a) {
        this.attributes_a = attributes_a;
    }

}