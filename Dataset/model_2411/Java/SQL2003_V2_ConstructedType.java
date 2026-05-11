





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V2_ConstructedType extends DataType {

    private String name;



    public SQL2003_V2_ConstructedType(
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