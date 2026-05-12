





import java.util.List;
import java.util.ArrayList;

public class rdbms_Constraints extends ModelElement {

    private String deferrable;
    private String deferred;



    public rdbms_Constraints(
        String deferrable,        String deferred    ) {
        super(
        );
        this.deferrable = deferrable;
        this.deferred = deferred;
    }


    public String getDeferrable() {
        return deferrable;
    }

    public void setDeferrable(String deferrable) {
        this.deferrable = deferrable;
    }
    public String getDeferred() {
        return deferred;
    }

    public void setDeferred(String deferred) {
        this.deferred = deferred;
    }


}