





import java.util.List;
import java.util.ArrayList;

public class rapidml_Parameter extends Extensible, RESTElement {

    private String default;
    private String name;
    private String fixed;
    private boolean required;



    public rapidml_Parameter(
        String default,        String name,        String fixed,        boolean required    ) {
        super(
        );
        this.default = default;
        this.name = name;
        this.fixed = fixed;
        this.required = required;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFixed() {
        return fixed;
    }

    public void setFixed(String fixed) {
        this.fixed = fixed;
    }
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }


}