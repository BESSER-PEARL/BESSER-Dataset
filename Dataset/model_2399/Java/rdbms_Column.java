





import java.util.List;
import java.util.ArrayList;

public class rdbms_Column  {

    private String type;
    private String name;





    private rdbms_Table rdbms_table;




    private rdbms_RDBMSModel rdbms_rdbmsmodel;




    private rdbms_Table rdbms_table;


    public rdbms_Column(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rdbms_Table getRdbms_table() {
        return rdbms_table;
    }

    public void setRdbms_table(rdbms_Table rdbms_table) {
        this.rdbms_table = rdbms_table;
    }
    public rdbms_RDBMSModel getRdbms_rdbmsmodel() {
        return rdbms_rdbmsmodel;
    }

    public void setRdbms_rdbmsmodel(rdbms_RDBMSModel rdbms_rdbmsmodel) {
        this.rdbms_rdbmsmodel = rdbms_rdbmsmodel;
    }
    public rdbms_Table getRdbms_table() {
        return rdbms_table;
    }

    public void setRdbms_table(rdbms_Table rdbms_table) {
        this.rdbms_table = rdbms_table;
    }

}