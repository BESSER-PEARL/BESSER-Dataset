





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsViewRelation  {

    private String name;





    private rdbms_RdbmsView rdbms_rdbmsview;




    private rdbms_RdbmsTableAlias rdbms_rdbmstablealias;




    private rdbms_RdbmsTableAlias rdbms_rdbmstablealias;




    private rdbms_RdbmsIdentifierField rdbms_rdbmsidentifierfield;




    private rdbms_RdbmsIdentifierField rdbms_rdbmsidentifierfield;


    public rdbms_RdbmsViewRelation(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rdbms_RdbmsView getRdbms_rdbmsview() {
        return rdbms_rdbmsview;
    }

    public void setRdbms_rdbmsview(rdbms_RdbmsView rdbms_rdbmsview) {
        this.rdbms_rdbmsview = rdbms_rdbmsview;
    }
    public rdbms_RdbmsTableAlias getRdbms_rdbmstablealias() {
        return rdbms_rdbmstablealias;
    }

    public void setRdbms_rdbmstablealias(rdbms_RdbmsTableAlias rdbms_rdbmstablealias) {
        this.rdbms_rdbmstablealias = rdbms_rdbmstablealias;
    }
    public rdbms_RdbmsTableAlias getRdbms_rdbmstablealias() {
        return rdbms_rdbmstablealias;
    }

    public void setRdbms_rdbmstablealias(rdbms_RdbmsTableAlias rdbms_rdbmstablealias) {
        this.rdbms_rdbmstablealias = rdbms_rdbmstablealias;
    }
    public rdbms_RdbmsIdentifierField getRdbms_rdbmsidentifierfield() {
        return rdbms_rdbmsidentifierfield;
    }

    public void setRdbms_rdbmsidentifierfield(rdbms_RdbmsIdentifierField rdbms_rdbmsidentifierfield) {
        this.rdbms_rdbmsidentifierfield = rdbms_rdbmsidentifierfield;
    }
    public rdbms_RdbmsIdentifierField getRdbms_rdbmsidentifierfield() {
        return rdbms_rdbmsidentifierfield;
    }

    public void setRdbms_rdbmsidentifierfield(rdbms_RdbmsIdentifierField rdbms_rdbmsidentifierfield) {
        this.rdbms_rdbmsidentifierfield = rdbms_rdbmsidentifierfield;
    }

}