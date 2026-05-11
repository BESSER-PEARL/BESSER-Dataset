





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsFieldType  {

    private int storageByte;
    private String description;
    private String name;
    private int scale;
    private String uuid;
    private String rdbmsTypeName;
    private int size;
    private int precision;





    private rdbms_RdbmsField rdbms_rdbmsfield;


    public rdbms_RdbmsFieldType(
        int storageByte,        String description,        String name,        int scale,        String uuid,        String rdbmsTypeName,        int size,        int precision    ) {
        this.storageByte = storageByte;
        this.description = description;
        this.name = name;
        this.scale = scale;
        this.uuid = uuid;
        this.rdbmsTypeName = rdbmsTypeName;
        this.size = size;
        this.precision = precision;
    }


    public int getStoragebyte() {
        return storageByte;
    }

    public void setStoragebyte(int storageByte) {
        this.storageByte = storageByte;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getScale() {
        return scale;
    }

    public void setScale(int scale) {
        this.scale = scale;
    }
    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }
    public String getRdbmstypename() {
        return rdbmsTypeName;
    }

    public void setRdbmstypename(String rdbmsTypeName) {
        this.rdbmsTypeName = rdbmsTypeName;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }

    public rdbms_RdbmsField getRdbms_rdbmsfield() {
        return rdbms_rdbmsfield;
    }

    public void setRdbms_rdbmsfield(rdbms_RdbmsField rdbms_rdbmsfield) {
        this.rdbms_rdbmsfield = rdbms_rdbmsfield;
    }

}