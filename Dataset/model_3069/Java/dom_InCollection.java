





import java.util.List;
import java.util.ArrayList;

public class dom_InCollection extends FromRange {

    private String alias;
    private String path;



    public dom_InCollection(
        String alias,        String path    ) {
        super(
        );
        this.alias = alias;
        this.path = path;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }


}