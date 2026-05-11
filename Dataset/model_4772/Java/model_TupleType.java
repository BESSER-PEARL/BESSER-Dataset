





import java.util.List;
import java.util.ArrayList;

public class model_TupleType extends Type {

    private String parts;



    public model_TupleType(
        String parts    ) {
        super(
        );
        this.parts = parts;
    }


    public String getParts() {
        return parts;
    }

    public void setParts(String parts) {
        this.parts = parts;
    }


}