





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_RdbmsModelElement  {

    private String rdbmsName;
    private String rdbmsKind;
    private String id;



    public SimpleRDBMS_RdbmsModelElement(
        String rdbmsName,        String rdbmsKind,        String id    ) {
        this.rdbmsName = rdbmsName;
        this.rdbmsKind = rdbmsKind;
        this.id = id;
    }


    public String getRdbmsname() {
        return rdbmsName;
    }

    public void setRdbmsname(String rdbmsName) {
        this.rdbmsName = rdbmsName;
    }
    public String getRdbmskind() {
        return rdbmsKind;
    }

    public void setRdbmskind(String rdbmsKind) {
        this.rdbmsKind = rdbmsKind;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}