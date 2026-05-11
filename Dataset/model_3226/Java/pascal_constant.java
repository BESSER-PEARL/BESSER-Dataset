





import java.util.List;
import java.util.ArrayList;

public class pascal_constant extends constant_definition {

    private String string;
    private String name;



    public pascal_constant(
        String string,        String name    ) {
        super(
        );
        this.string = string;
        this.name = name;
    }


    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}