





import java.util.List;
import java.util.ArrayList;

public class rdbmdl_view_View extends NamedColumnSet {

    private String ddl;



    public rdbmdl_view_View(
        String ddl    ) {
        super(
        );
        this.ddl = ddl;
    }


    public String getDdl() {
        return ddl;
    }

    public void setDdl(String ddl) {
        this.ddl = ddl;
    }


}