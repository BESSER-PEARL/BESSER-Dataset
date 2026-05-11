





import java.util.List;
import java.util.ArrayList;

public class build_StringProperties  {

    private boolean immutable;
    private String value;
    private String key;





    private build_PropertyScope build_propertyscope;


    public build_StringProperties(
        boolean immutable,        String value,        String key    ) {
        this.immutable = immutable;
        this.value = value;
        this.key = key;
    }


    public boolean getImmutable() {
        return immutable;
    }

    public void setImmutable(boolean immutable) {
        this.immutable = immutable;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public build_PropertyScope getBuild_propertyscope() {
        return build_propertyscope;
    }

    public void setBuild_propertyscope(build_PropertyScope build_propertyscope) {
        this.build_propertyscope = build_propertyscope;
    }

}