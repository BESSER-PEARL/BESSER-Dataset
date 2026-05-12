





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_Create extends DdlStatement {

    private String name;



    public ddlDsl_Create(
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