





import java.util.List;
import java.util.ArrayList;

public class ric_FormControl extends ClassifiableComponent, IdentifiableComponent, EventComponent {

    private String value;
    private String name;



    public ric_FormControl(
        String value,        String name    ) {
        super(
        );
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


}