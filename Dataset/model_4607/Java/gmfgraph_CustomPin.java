





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_CustomPin extends Pin {

    private String customOperationType;
    private String customOperationName;



    public gmfgraph_CustomPin(
        String customOperationType,        String customOperationName    ) {
        super(
        );
        this.customOperationType = customOperationType;
        this.customOperationName = customOperationName;
    }


    public String getCustomoperationtype() {
        return customOperationType;
    }

    public void setCustomoperationtype(String customOperationType) {
        this.customOperationType = customOperationType;
    }
    public String getCustomoperationname() {
        return customOperationName;
    }

    public void setCustomoperationname(String customOperationName) {
        this.customOperationName = customOperationName;
    }


}