





import java.util.List;
import java.util.ArrayList;

public class railDsl_Vertex extends Declaration {

    private String kind;



    public railDsl_Vertex(
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