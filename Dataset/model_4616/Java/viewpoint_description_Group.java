





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_Group extends description_DModelElement, description_DocumentedElement {

    private String version;
    private String name;



    public viewpoint_description_Group(
        String version,        String name    ) {
        super(
        );
        this.version = version;
        this.name = name;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}