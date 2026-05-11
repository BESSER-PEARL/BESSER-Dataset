





import java.util.List;
import java.util.ArrayList;

public class r1_Property extends Expression {

    private String path;
    private String scope;



    public r1_Property(
        String path,        String scope    ) {
        super(
        );
        this.path = path;
        this.scope = scope;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }


}