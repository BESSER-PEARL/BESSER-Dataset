





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Parameter extends TypedElement {

    private String name;



    public ClassDiagram_Parameter(
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