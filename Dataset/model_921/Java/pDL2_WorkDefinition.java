





import java.util.List;
import java.util.ArrayList;

public class pDL2_WorkDefinition extends ProcessElement {

    private String name;



    public pDL2_WorkDefinition(
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