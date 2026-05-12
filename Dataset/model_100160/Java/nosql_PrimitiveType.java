





import java.util.List;
import java.util.ArrayList;

public class nosql_PrimitiveType extends Type {

    private String kind;



    public nosql_PrimitiveType(
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