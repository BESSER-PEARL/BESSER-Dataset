





import java.util.List;
import java.util.ArrayList;

public class sqls_SqlParam extends SqlExpr {

    private String name;



    public sqls_SqlParam(
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