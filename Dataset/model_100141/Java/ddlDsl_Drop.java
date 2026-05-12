





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_Drop extends DdlStatement {

    private String object;



    public ddlDsl_Drop(
        String object    ) {
        super(
        );
        this.object = object;
    }


    public String getObject() {
        return object;
    }

    public void setObject(String object) {
        this.object = object;
    }


}