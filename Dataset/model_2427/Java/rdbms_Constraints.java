





import java.util.List;
import java.util.ArrayList;

public class rdbms_Constraints extends ModelElement {

    private String deferred;
    private String deferrable;



    public rdbms_Constraints(
        String deferred,        String deferrable    ) {
        super(
        );
        this.deferred = deferred;
        this.deferrable = deferrable;
    }


    public String getDeferred() {
        return deferred;
    }

    public void setDeferred(String deferred) {
        this.deferred = deferred;
    }
    public String getDeferrable() {
        return deferrable;
    }

    public void setDeferrable(String deferrable) {
        this.deferrable = deferrable;
    }


}