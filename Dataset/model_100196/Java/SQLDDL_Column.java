





import java.util.List;
import java.util.ArrayList;

public class SQLDDL_Column extends TableElement {

    private String canBeNull;
    private String name;



    public SQLDDL_Column(
        String canBeNull,        String name    ) {
        super(
        );
        this.canBeNull = canBeNull;
        this.name = name;
    }


    public String getCanbenull() {
        return canBeNull;
    }

    public void setCanbenull(String canBeNull) {
        this.canBeNull = canBeNull;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}