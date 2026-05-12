





import java.util.List;
import java.util.ArrayList;

public class ASM_ElementDecl extends LocatedElement {

    private String name;



    public ASM_ElementDecl(
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