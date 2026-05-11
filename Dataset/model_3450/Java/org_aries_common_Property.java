





import java.util.List;
import java.util.ArrayList;

public class org_aries_common_Property  {

    private String name;
    private String id;
    private String mixed;
    private String value;



    public org_aries_common_Property(
        String name,        String id,        String mixed,        String value    ) {
        this.name = name;
        this.id = id;
        this.mixed = mixed;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}