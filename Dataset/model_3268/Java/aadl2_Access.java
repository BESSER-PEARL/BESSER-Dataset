





import java.util.List;
import java.util.ArrayList;

public class aadl2_Access extends AccessConnectionEnd, Feature {

    private String category;
    private String kind;



    public aadl2_Access(
        String category,        String kind    ) {
        super(
        );
        this.category = category;
        this.kind = kind;
    }


    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}