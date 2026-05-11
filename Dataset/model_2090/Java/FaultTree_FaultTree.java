





import java.util.List;
import java.util.ArrayList;

public class FaultTree_FaultTree  {

    private String message;
    private String name;
    private String faultTreeType;



    public FaultTree_FaultTree(
        String message,        String name,        String faultTreeType    ) {
        this.message = message;
        this.name = name;
        this.faultTreeType = faultTreeType;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFaulttreetype() {
        return faultTreeType;
    }

    public void setFaulttreetype(String faultTreeType) {
        this.faultTreeType = faultTreeType;
    }


}