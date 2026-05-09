





import java.util.List;
import java.util.ArrayList;

public class pDL1_WorkDefinition extends ProcessElement {

    private String name;



    public pDL1_WorkDefinition(
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