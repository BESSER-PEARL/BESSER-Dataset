





import java.util.List;
import java.util.ArrayList;

public class sqlDSL_SColumn extends STableMember {

    private String simpleType;



    public sqlDSL_SColumn(
        String simpleType    ) {
        super(
        );
        this.simpleType = simpleType;
    }


    public String getSimpletype() {
        return simpleType;
    }

    public void setSimpletype(String simpleType) {
        this.simpleType = simpleType;
    }


}