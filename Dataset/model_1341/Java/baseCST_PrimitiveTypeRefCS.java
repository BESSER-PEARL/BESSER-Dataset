





import java.util.List;
import java.util.ArrayList;

public class baseCST_PrimitiveTypeRefCS extends TypedRefCS, Nameable {

    private String name;



    public baseCST_PrimitiveTypeRefCS(
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