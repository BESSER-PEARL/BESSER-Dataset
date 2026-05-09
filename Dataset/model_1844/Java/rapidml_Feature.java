





import java.util.List;
import java.util.ArrayList;

public class rapidml_Feature extends Extensible, Documentable, Element {

    private boolean restriction;
    private boolean readOnly;
    private String name;
    private boolean key;



    public rapidml_Feature(
        boolean restriction,        boolean readOnly,        String name,        boolean key    ) {
        super(
        );
        this.restriction = restriction;
        this.readOnly = readOnly;
        this.name = name;
        this.key = key;
    }


    public boolean getRestriction() {
        return restriction;
    }

    public void setRestriction(boolean restriction) {
        this.restriction = restriction;
    }
    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getKey() {
        return key;
    }

    public void setKey(boolean key) {
        this.key = key;
    }


}