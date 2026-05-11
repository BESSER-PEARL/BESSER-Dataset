





import java.util.List;
import java.util.ArrayList;

public class iso20022_SchemaType extends DataType {

    private String kind;



    public iso20022_SchemaType(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}