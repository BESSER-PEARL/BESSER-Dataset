





import java.util.List;
import java.util.ArrayList;

public class dom_Property extends IDocumentable, ReferenceableByXmadslVariable {

    private String name;
    private String defaultValue;





    private dom_ApplicationSession dom_applicationsession;


    public dom_Property(
        String name,        String defaultValue    ) {
        super(
        );
        this.name = name;
        this.defaultValue = defaultValue;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }

    public dom_ApplicationSession getDom_applicationsession() {
        return dom_applicationsession;
    }

    public void setDom_applicationsession(dom_ApplicationSession dom_applicationsession) {
        this.dom_applicationsession = dom_applicationsession;
    }

}