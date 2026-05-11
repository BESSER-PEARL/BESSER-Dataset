





import java.util.List;
import java.util.ArrayList;

public class oogen_OOEnumeration extends OOCommentOwner {

    private String options;
    private String name;



    public oogen_OOEnumeration(
        String options,        String name    ) {
        super(
        );
        this.options = options;
        this.name = name;
    }


    public String getOptions() {
        return options;
    }

    public void setOptions(String options) {
        this.options = options;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}