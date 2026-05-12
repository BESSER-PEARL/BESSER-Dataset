





import java.util.List;
import java.util.ArrayList;

public class AsmL_Parameter extends LocatedElement {

    private String name;



    public AsmL_Parameter(
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