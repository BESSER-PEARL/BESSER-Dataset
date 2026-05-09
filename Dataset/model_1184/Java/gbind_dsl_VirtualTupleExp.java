





import java.util.List;
import java.util.ArrayList;

public class gbind_dsl_VirtualTupleExp extends TupleExp {

    private String typeName;



    public gbind_dsl_VirtualTupleExp(
        String typeName    ) {
        super(
        );
        this.typeName = typeName;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }


}