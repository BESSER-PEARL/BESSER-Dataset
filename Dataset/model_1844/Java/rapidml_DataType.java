





import java.util.List;
import java.util.ArrayList;

public class rapidml_DataType extends Extensible, Documentable {

    private String name;



    public rapidml_DataType(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}