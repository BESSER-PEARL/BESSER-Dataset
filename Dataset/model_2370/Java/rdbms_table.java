





import java.util.List;
import java.util.ArrayList;

public class rdbms_table  {

    private String oID;
    private String name;
    private String kind;





    private rdbms_columns rdbms_columns;




    private rdbms_DocumentRoot rdbms_documentroot;




    private rdbms_key2 rdbms_key2;


    public rdbms_table(
        String oID,        String name,        String kind    ) {
        this.oID = oID;
        this.name = name;
        this.kind = kind;
    }


    public String getOid() {
        return oID;
    }

    public void setOid(String oID) {
        this.oID = oID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public rdbms_columns getRdbms_columns() {
        return rdbms_columns;
    }

    public void setRdbms_columns(rdbms_columns rdbms_columns) {
        this.rdbms_columns = rdbms_columns;
    }
    public rdbms_DocumentRoot getRdbms_documentroot() {
        return rdbms_documentroot;
    }

    public void setRdbms_documentroot(rdbms_DocumentRoot rdbms_documentroot) {
        this.rdbms_documentroot = rdbms_documentroot;
    }
    public rdbms_key2 getRdbms_key2() {
        return rdbms_key2;
    }

    public void setRdbms_key2(rdbms_key2 rdbms_key2) {
        this.rdbms_key2 = rdbms_key2;
    }

}