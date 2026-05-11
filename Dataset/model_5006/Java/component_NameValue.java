





import java.util.List;
import java.util.ArrayList;

public class component_NameValue extends WrapperObject {

    private String value;
    private String typeName;
    private String name;





    private component_ConfigurationSet component_configurationset;


    public component_NameValue(
        String value,        String typeName,        String name    ) {
        super(
        );
        this.value = value;
        this.typeName = typeName;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public component_ConfigurationSet getComponent_configurationset() {
        return component_configurationset;
    }

    public void setComponent_configurationset(component_ConfigurationSet component_configurationset) {
        this.component_configurationset = component_configurationset;
    }

}