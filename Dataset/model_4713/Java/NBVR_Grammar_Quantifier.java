





import java.util.List;
import java.util.ArrayList;

public class NBVR_Grammar_Quantifier extends ParseElement {

    private int count;
    private String kind;



    public NBVR_Grammar_Quantifier(
        int count,        String kind    ) {
        super(
        );
        this.count = count;
        this.kind = kind;
    }


    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}