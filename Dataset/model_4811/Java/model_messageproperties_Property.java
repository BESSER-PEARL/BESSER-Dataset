





import java.util.List;
import java.util.ArrayList;

public class model_messageproperties_Property extends ExtensibilityElement {

    private String ID;
    private String name;
    private String qName;
    private String type;



    public model_messageproperties_Property(
        String ID,        String name,        String qName,        String type    ) {
        super(
        );
        this.ID = ID;
        this.name = name;
        this.qName = qName;
        this.type = type;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getQname() {
        return qName;
    }

    public void setQname(String qName) {
        this.qName = qName;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}