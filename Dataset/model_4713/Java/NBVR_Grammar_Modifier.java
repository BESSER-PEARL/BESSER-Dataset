





import java.util.List;
import java.util.ArrayList;

public class NBVR_Grammar_Modifier extends ParseElement {

    private String kind;



    public NBVR_Grammar_Modifier(
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