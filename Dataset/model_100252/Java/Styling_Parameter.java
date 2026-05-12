





import java.util.List;
import java.util.ArrayList;

public class Styling_Parameter  {

    private String name;





    private Styling_OperationPattern styling_operationpattern;


    public Styling_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Styling_OperationPattern getStyling_operationpattern() {
        return styling_operationpattern;
    }

    public void setStyling_operationpattern(Styling_OperationPattern styling_operationpattern) {
        this.styling_operationpattern = styling_operationpattern;
    }

}