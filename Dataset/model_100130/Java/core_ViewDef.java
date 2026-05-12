





import java.util.List;
import java.util.ArrayList;

public class core_ViewDef extends TableDef {

    private String querySelect;



    public core_ViewDef(
        String querySelect    ) {
        super(
        );
        this.querySelect = querySelect;
    }


    public String getQueryselect() {
        return querySelect;
    }

    public void setQueryselect(String querySelect) {
        this.querySelect = querySelect;
    }


}