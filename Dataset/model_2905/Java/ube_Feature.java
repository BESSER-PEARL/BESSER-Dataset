





import java.util.List;
import java.util.ArrayList;

public class ube_Feature extends NamedElement {

    private String kind;





    private ube_Type ube_type;


    public ube_Feature(
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

    public ube_Type getUbe_type() {
        return ube_type;
    }

    public void setUbe_type(ube_Type ube_type) {
        this.ube_type = ube_type;
    }

}