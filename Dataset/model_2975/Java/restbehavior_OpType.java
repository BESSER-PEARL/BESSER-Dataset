





import java.util.List;
import java.util.ArrayList;

public class restbehavior_OpType  {

    private String name;





    private restbehavior_DataType restbehavior_datatype;


    public restbehavior_OpType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public restbehavior_DataType getRestbehavior_datatype() {
        return restbehavior_datatype;
    }

    public void setRestbehavior_datatype(restbehavior_DataType restbehavior_datatype) {
        this.restbehavior_datatype = restbehavior_datatype;
    }

}