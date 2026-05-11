





import java.util.List;
import java.util.ArrayList;

public class thingML_Parameter extends AnnotatedElement, ReferencedElmt, Variable {

    private String name;



    public thingML_Parameter(
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