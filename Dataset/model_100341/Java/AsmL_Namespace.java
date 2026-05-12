





import java.util.List;
import java.util.ArrayList;

public class AsmL_Namespace extends AsmLElement {

    private String name;



    public AsmL_Namespace(
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