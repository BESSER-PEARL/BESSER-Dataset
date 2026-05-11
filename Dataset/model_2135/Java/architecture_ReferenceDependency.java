





import java.util.List;
import java.util.ArrayList;

public class architecture_ReferenceDependency extends Dependency {

    private String name;
    private String uri;



    public architecture_ReferenceDependency(
        String name,        String uri    ) {
        super(
        );
        this.name = name;
        this.uri = uri;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }


}