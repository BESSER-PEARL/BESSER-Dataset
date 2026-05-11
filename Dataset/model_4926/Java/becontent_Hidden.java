





import java.util.List;
import java.util.ArrayList;

public class becontent_Hidden extends NotStructuredElement {

    private String name;
    private String values;



    public becontent_Hidden(
        String name,        String values    ) {
        super(
        );
        this.name = name;
        this.values = values;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
    }


}