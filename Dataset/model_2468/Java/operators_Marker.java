





import java.util.List;
import java.util.ArrayList;

public class operators_Marker extends Base {

    private String description;
    private String kind;



    public operators_Marker(
        String description,        String kind    ) {
        super(
        );
        this.description = description;
        this.kind = kind;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}