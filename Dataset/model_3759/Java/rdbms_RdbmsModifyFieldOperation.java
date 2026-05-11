





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsModifyFieldOperation extends RdbmsFieldOperation {

    private String changedForeignKeyToValueField;
    private String changedValueFieldToForeignKey;
    private boolean typeChanged;
    private boolean mandatoryChanged;
    private String sizeChanged;
    private String nameChanged;





    private rdbms_RdbmsField rdbms_rdbmsfield;




    private rdbms_RdbmsModifyTableOperation rdbms_rdbmsmodifytableoperation;


    public rdbms_RdbmsModifyFieldOperation(
        String changedForeignKeyToValueField,        String changedValueFieldToForeignKey,        boolean typeChanged,        boolean mandatoryChanged,        String sizeChanged,        String nameChanged    ) {
        super(
        );
        this.changedForeignKeyToValueField = changedForeignKeyToValueField;
        this.changedValueFieldToForeignKey = changedValueFieldToForeignKey;
        this.typeChanged = typeChanged;
        this.mandatoryChanged = mandatoryChanged;
        this.sizeChanged = sizeChanged;
        this.nameChanged = nameChanged;
    }


    public String getChangedforeignkeytovaluefield() {
        return changedForeignKeyToValueField;
    }

    public void setChangedforeignkeytovaluefield(String changedForeignKeyToValueField) {
        this.changedForeignKeyToValueField = changedForeignKeyToValueField;
    }
    public String getChangedvaluefieldtoforeignkey() {
        return changedValueFieldToForeignKey;
    }

    public void setChangedvaluefieldtoforeignkey(String changedValueFieldToForeignKey) {
        this.changedValueFieldToForeignKey = changedValueFieldToForeignKey;
    }
    public boolean getTypechanged() {
        return typeChanged;
    }

    public void setTypechanged(boolean typeChanged) {
        this.typeChanged = typeChanged;
    }
    public boolean getMandatorychanged() {
        return mandatoryChanged;
    }

    public void setMandatorychanged(boolean mandatoryChanged) {
        this.mandatoryChanged = mandatoryChanged;
    }
    public String getSizechanged() {
        return sizeChanged;
    }

    public void setSizechanged(String sizeChanged) {
        this.sizeChanged = sizeChanged;
    }
    public String getNamechanged() {
        return nameChanged;
    }

    public void setNamechanged(String nameChanged) {
        this.nameChanged = nameChanged;
    }

    public rdbms_RdbmsField getRdbms_rdbmsfield() {
        return rdbms_rdbmsfield;
    }

    public void setRdbms_rdbmsfield(rdbms_RdbmsField rdbms_rdbmsfield) {
        this.rdbms_rdbmsfield = rdbms_rdbmsfield;
    }
    public rdbms_RdbmsModifyTableOperation getRdbms_rdbmsmodifytableoperation() {
        return rdbms_rdbmsmodifytableoperation;
    }

    public void setRdbms_rdbmsmodifytableoperation(rdbms_RdbmsModifyTableOperation rdbms_rdbmsmodifytableoperation) {
        this.rdbms_rdbmsmodifytableoperation = rdbms_rdbmsmodifytableoperation;
    }

}