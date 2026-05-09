





import java.util.List;
import java.util.ArrayList;

public class pivot_CollectionLiteralExp extends LiteralExp {

    private String kind;



    public pivot_CollectionLiteralExp(
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