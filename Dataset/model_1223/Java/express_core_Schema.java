





import java.util.List;
import java.util.ArrayList;

public class express_core_Schema extends Scope {

    private String name;
    private String version;



    public express_core_Schema(
        String name,        String version    ) {
        super(
        );
        this.name = name;
        this.version = version;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}