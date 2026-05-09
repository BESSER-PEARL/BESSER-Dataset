





import java.util.List;
import java.util.ArrayList;

public class baseCST_NamedElementCS extends Nameable, ModelElementCS {

    private String name;



    public baseCST_NamedElementCS(
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