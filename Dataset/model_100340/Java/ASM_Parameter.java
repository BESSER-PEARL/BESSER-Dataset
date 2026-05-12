





import java.util.List;
import java.util.ArrayList;

public class ASM_Parameter extends LocatedElement {

    private String type;
    private String name;



    public ASM_Parameter(
        String type,        String name    ) {
        super(
        );
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}