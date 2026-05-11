





import java.util.List;
import java.util.ArrayList;

public class r1_NamedTypeSpecifier extends TypeSpecifier {

    private String name;



    public r1_NamedTypeSpecifier(
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