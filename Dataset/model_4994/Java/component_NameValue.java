





import java.util.List;
import java.util.ArrayList;

public class component_NameValue extends WrapperObject {

    private String value;
    private String name;
    private String typeName;



    public component_NameValue(
        String value,        String name,        String typeName    ) {
        super(
        );
        this.value = value;
        this.name = name;
        this.typeName = typeName;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }


}