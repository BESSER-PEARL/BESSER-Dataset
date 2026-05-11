





import java.util.List;
import java.util.ArrayList;

public class fM_Node extends Child {

    private String close_relation;
    private String open_relation;



    public fM_Node(
        String close_relation,        String open_relation    ) {
        super(
        );
        this.close_relation = close_relation;
        this.open_relation = open_relation;
    }


    public String getClose_relation() {
        return close_relation;
    }

    public void setClose_relation(String close_relation) {
        this.close_relation = close_relation;
    }
    public String getOpen_relation() {
        return open_relation;
    }

    public void setOpen_relation(String open_relation) {
        this.open_relation = open_relation;
    }


}