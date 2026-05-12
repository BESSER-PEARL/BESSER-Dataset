





import java.util.List;
import java.util.ArrayList;

public class build_PropertyScope  {

    private String unsetProperties;





    private build_StringProperties build_stringproperties;


    public build_PropertyScope(
        String unsetProperties    ) {
        this.unsetProperties = unsetProperties;
    }


    public String getUnsetproperties() {
        return unsetProperties;
    }

    public void setUnsetproperties(String unsetProperties) {
        this.unsetProperties = unsetProperties;
    }

    public build_StringProperties getBuild_stringproperties() {
        return build_stringproperties;
    }

    public void setBuild_stringproperties(build_StringProperties build_stringproperties) {
        this.build_stringproperties = build_stringproperties;
    }

}