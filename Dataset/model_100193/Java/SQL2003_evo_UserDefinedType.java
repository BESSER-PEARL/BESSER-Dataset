





import java.util.List;
import java.util.ArrayList;

public class SQL2003_evo_UserDefinedType extends DataType {

    private String name;



    public SQL2003_evo_UserDefinedType(
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