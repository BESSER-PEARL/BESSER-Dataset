





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsField extends RdbmsElement {

    private int storageByte;
    private int scale;
    private int size;
    private boolean mandatory;
    private int precision;
    private String rdbmsTypeName;





    private rdbms_RdbmsFieldOperation rdbms_rdbmsfieldoperation;




    private rdbms_RdbmsUniqueConstraint rdbms_rdbmsuniqueconstraint;




    private rdbms_RdbmsTable rdbms_rdbmstable;




    private rdbms_RdbmsTable rdbms_rdbmstable;




    private rdbms_RdbmsIndex rdbms_rdbmsindex;


    public rdbms_RdbmsField(
        int storageByte,        int scale,        int size,        boolean mandatory,        int precision,        String rdbmsTypeName    ) {
        super(
        );
        this.storageByte = storageByte;
        this.scale = scale;
        this.size = size;
        this.mandatory = mandatory;
        this.precision = precision;
        this.rdbmsTypeName = rdbmsTypeName;
    }


    public int getStoragebyte() {
        return storageByte;
    }

    public void setStoragebyte(int storageByte) {
        this.storageByte = storageByte;
    }
    public int getScale() {
        return scale;
    }

    public void setScale(int scale) {
        this.scale = scale;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }
    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }
    public String getRdbmstypename() {
        return rdbmsTypeName;
    }

    public void setRdbmstypename(String rdbmsTypeName) {
        this.rdbmsTypeName = rdbmsTypeName;
    }

    public rdbms_RdbmsFieldOperation getRdbms_rdbmsfieldoperation() {
        return rdbms_rdbmsfieldoperation;
    }

    public void setRdbms_rdbmsfieldoperation(rdbms_RdbmsFieldOperation rdbms_rdbmsfieldoperation) {
        this.rdbms_rdbmsfieldoperation = rdbms_rdbmsfieldoperation;
    }
    public rdbms_RdbmsUniqueConstraint getRdbms_rdbmsuniqueconstraint() {
        return rdbms_rdbmsuniqueconstraint;
    }

    public void setRdbms_rdbmsuniqueconstraint(rdbms_RdbmsUniqueConstraint rdbms_rdbmsuniqueconstraint) {
        this.rdbms_rdbmsuniqueconstraint = rdbms_rdbmsuniqueconstraint;
    }
    public rdbms_RdbmsTable getRdbms_rdbmstable() {
        return rdbms_rdbmstable;
    }

    public void setRdbms_rdbmstable(rdbms_RdbmsTable rdbms_rdbmstable) {
        this.rdbms_rdbmstable = rdbms_rdbmstable;
    }
    public rdbms_RdbmsTable getRdbms_rdbmstable() {
        return rdbms_rdbmstable;
    }

    public void setRdbms_rdbmstable(rdbms_RdbmsTable rdbms_rdbmstable) {
        this.rdbms_rdbmstable = rdbms_rdbmstable;
    }
    public rdbms_RdbmsIndex getRdbms_rdbmsindex() {
        return rdbms_rdbmsindex;
    }

    public void setRdbms_rdbmsindex(rdbms_RdbmsIndex rdbms_rdbmsindex) {
        this.rdbms_rdbmsindex = rdbms_rdbmsindex;
    }

}