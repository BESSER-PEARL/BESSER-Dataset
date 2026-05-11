





import java.util.List;
import java.util.ArrayList;

public class type_EnumAttribute extends Categorized {

    private String name;
    private String value;
    private String uid;





    private type_Enumerator type_enumerator;


    public type_EnumAttribute(
        String name,        String value,        String uid    ) {
        super(
        );
        this.name = name;
        this.value = value;
        this.uid = uid;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public type_Enumerator getType_enumerator() {
        return type_enumerator;
    }

    public void setType_enumerator(type_Enumerator type_enumerator) {
        this.type_enumerator = type_enumerator;
    }

}