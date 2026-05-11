





import java.util.List;
import java.util.ArrayList;

public class componentBasedSystem_dataTypes_Simple extends dataTypes_ParameterType, dataTypes_ReturnType {

    private String kind;



    public componentBasedSystem_dataTypes_Simple(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}