





import java.util.List;
import java.util.ArrayList;

public class thingML_Instance extends AnnotatedElement {

    private String name;



    public thingML_Instance(
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