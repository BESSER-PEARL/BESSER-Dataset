





import java.util.List;
import java.util.ArrayList;

public class sql_datatype_BinaryLargeObjectStringType extends PredefinedType {

    private String kind;



    public sql_datatype_BinaryLargeObjectStringType(
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