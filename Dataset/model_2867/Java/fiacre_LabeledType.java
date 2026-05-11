





import java.util.List;
import java.util.ArrayList;

public class fiacre_LabeledType  {

    private String name;





    private fiacre_Type fiacre_type;


    public fiacre_LabeledType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fiacre_Type getFiacre_type() {
        return fiacre_type;
    }

    public void setFiacre_type(fiacre_Type fiacre_type) {
        this.fiacre_type = fiacre_type;
    }

}