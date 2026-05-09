





import java.util.List;
import java.util.ArrayList;

public class occi_Attribute extends AnnotatedElement {

    private String description;
    private String default;
    private String mutable;
    private String name;
    private String required;



    public occi_Attribute(
        String description,        String default,        String mutable,        String name,        String required    ) {
        super(
        );
        this.description = description;
        this.default = default;
        this.mutable = mutable;
        this.name = name;
        this.required = required;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getMutable() {
        return mutable;
    }

    public void setMutable(String mutable) {
        this.mutable = mutable;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRequired() {
        return required;
    }

    public void setRequired(String required) {
        this.required = required;
    }


}