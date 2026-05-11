





import java.util.List;
import java.util.ArrayList;

public class scxml_HistoryState extends NamedElement {

    private String id;
    private String type;





    private scxml_Parallel scxml_parallel;


    public scxml_HistoryState(
        String id,        String type    ) {
        super(
        );
        this.id = id;
        this.type = type;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public scxml_Parallel getScxml_parallel() {
        return scxml_parallel;
    }

    public void setScxml_parallel(scxml_Parallel scxml_parallel) {
        this.scxml_parallel = scxml_parallel;
    }

}