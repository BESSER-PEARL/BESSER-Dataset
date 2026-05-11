





import java.util.List;
import java.util.ArrayList;

public class modelDsl_Enumerable extends ModelType {

    private String enums;



    public modelDsl_Enumerable(
        String enums    ) {
        super(
        );
        this.enums = enums;
    }


    public String getEnums() {
        return enums;
    }

    public void setEnums(String enums) {
        this.enums = enums;
    }


}