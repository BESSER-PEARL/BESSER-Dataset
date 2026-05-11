





import java.util.List;
import java.util.ArrayList;

public class simpleumltordbms_PrimitiveToName extends UmlToRdbmsModelElement {

    private String typeName;



    public simpleumltordbms_PrimitiveToName(
        String typeName    ) {
        super(
        );
        this.typeName = typeName;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }


}