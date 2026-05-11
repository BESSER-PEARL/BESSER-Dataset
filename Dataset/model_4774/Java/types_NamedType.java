





import java.util.List;
import java.util.ArrayList;

public class types_NamedType extends Type {

    private String name;



    public types_NamedType(
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