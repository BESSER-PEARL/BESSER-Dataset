





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsForeignKey extends RdbmsIdentifierField {

    private boolean inheritenceBased;
    private boolean readOnly;
    private boolean deferred;
    private String foreignKeySqlName;
    private boolean deleteOnCascade;





    private rdbms_RdbmsIdentifierField rdbms_rdbmsidentifierfield;




    private rdbms_RdbmsJunctionTable rdbms_rdbmsjunctiontable;




    private rdbms_RdbmsJunctionTable rdbms_rdbmsjunctiontable;




    private rdbms_RdbmsIdentifierField rdbms_rdbmsidentifierfield;


    public rdbms_RdbmsForeignKey(
        boolean inheritenceBased,        boolean readOnly,        boolean deferred,        String foreignKeySqlName,        boolean deleteOnCascade    ) {
        super(
        );
        this.inheritenceBased = inheritenceBased;
        this.readOnly = readOnly;
        this.deferred = deferred;
        this.foreignKeySqlName = foreignKeySqlName;
        this.deleteOnCascade = deleteOnCascade;
    }


    public boolean getInheritencebased() {
        return inheritenceBased;
    }

    public void setInheritencebased(boolean inheritenceBased) {
        this.inheritenceBased = inheritenceBased;
    }
    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }
    public boolean getDeferred() {
        return deferred;
    }

    public void setDeferred(boolean deferred) {
        this.deferred = deferred;
    }
    public String getForeignkeysqlname() {
        return foreignKeySqlName;
    }

    public void setForeignkeysqlname(String foreignKeySqlName) {
        this.foreignKeySqlName = foreignKeySqlName;
    }
    public boolean getDeleteoncascade() {
        return deleteOnCascade;
    }

    public void setDeleteoncascade(boolean deleteOnCascade) {
        this.deleteOnCascade = deleteOnCascade;
    }

    public rdbms_RdbmsIdentifierField getRdbms_rdbmsidentifierfield() {
        return rdbms_rdbmsidentifierfield;
    }

    public void setRdbms_rdbmsidentifierfield(rdbms_RdbmsIdentifierField rdbms_rdbmsidentifierfield) {
        this.rdbms_rdbmsidentifierfield = rdbms_rdbmsidentifierfield;
    }
    public rdbms_RdbmsJunctionTable getRdbms_rdbmsjunctiontable() {
        return rdbms_rdbmsjunctiontable;
    }

    public void setRdbms_rdbmsjunctiontable(rdbms_RdbmsJunctionTable rdbms_rdbmsjunctiontable) {
        this.rdbms_rdbmsjunctiontable = rdbms_rdbmsjunctiontable;
    }
    public rdbms_RdbmsJunctionTable getRdbms_rdbmsjunctiontable() {
        return rdbms_rdbmsjunctiontable;
    }

    public void setRdbms_rdbmsjunctiontable(rdbms_RdbmsJunctionTable rdbms_rdbmsjunctiontable) {
        this.rdbms_rdbmsjunctiontable = rdbms_rdbmsjunctiontable;
    }
    public rdbms_RdbmsIdentifierField getRdbms_rdbmsidentifierfield() {
        return rdbms_rdbmsidentifierfield;
    }

    public void setRdbms_rdbmsidentifierfield(rdbms_RdbmsIdentifierField rdbms_rdbmsidentifierfield) {
        this.rdbms_rdbmsidentifierfield = rdbms_rdbmsidentifierfield;
    }

}