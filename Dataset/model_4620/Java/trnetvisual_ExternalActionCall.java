





import java.util.List;
import java.util.ArrayList;

public class trnetvisual_ExternalActionCall extends Action {

    private String id;
    private String qualifiedName;



    public trnetvisual_ExternalActionCall(
        String id,        String qualifiedName    ) {
        super(
        );
        this.id = id;
        this.qualifiedName = qualifiedName;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }


}