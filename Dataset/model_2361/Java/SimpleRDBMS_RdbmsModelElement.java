





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_RdbmsModelElement  {

    private String id;
    private String rdbmsKind;
    private String rdbmsName;



    public SimpleRDBMS_RdbmsModelElement(
        String id,        String rdbmsKind,        String rdbmsName    ) {
        this.id = id;
        this.rdbmsKind = rdbmsKind;
        this.rdbmsName = rdbmsName;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getRdbmskind() {
        return rdbmsKind;
    }

    public void setRdbmskind(String rdbmsKind) {
        this.rdbmsKind = rdbmsKind;
    }
    public String getRdbmsname() {
        return rdbmsName;
    }

    public void setRdbmsname(String rdbmsName) {
        this.rdbmsName = rdbmsName;
    }


}