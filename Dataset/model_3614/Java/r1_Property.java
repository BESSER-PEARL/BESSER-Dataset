





import java.util.List;
import java.util.ArrayList;

public class r1_Property extends Expression {

    private String scope;
    private String path;



    public r1_Property(
        String scope,        String path    ) {
        super(
        );
        this.scope = scope;
        this.path = path;
    }


    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }


}