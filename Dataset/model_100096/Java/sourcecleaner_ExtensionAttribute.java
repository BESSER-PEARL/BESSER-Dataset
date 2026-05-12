





import java.util.List;
import java.util.ArrayList;

public class sourcecleaner_ExtensionAttribute  {

    private String value;
    private String name;





    private sourcecleaner_Extension sourcecleaner_extension;


    public sourcecleaner_ExtensionAttribute(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
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

    public sourcecleaner_Extension getSourcecleaner_extension() {
        return sourcecleaner_extension;
    }

    public void setSourcecleaner_extension(sourcecleaner_Extension sourcecleaner_extension) {
        this.sourcecleaner_extension = sourcecleaner_extension;
    }

}