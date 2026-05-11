





import java.util.List;
import java.util.ArrayList;

public class modelDsl_DefLinkVariable extends DefIdAttribute {

    private String name;





    private modelDsl_Link modeldsl_link;


    public modelDsl_DefLinkVariable(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public modelDsl_Link getModeldsl_link() {
        return modeldsl_link;
    }

    public void setModeldsl_link(modelDsl_Link modeldsl_link) {
        this.modeldsl_link = modeldsl_link;
    }

}