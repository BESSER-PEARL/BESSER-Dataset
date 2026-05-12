





import java.util.List;
import java.util.ArrayList;

public class core_TableColumnDef extends DatabaseObjectDef {

    private int scale;
    private boolean default;
    private boolean nullable;
    private int length;
    private String name;
    private String dataType;





    private core_TableDef core_tabledef;


    public core_TableColumnDef(
        int scale,        boolean default,        boolean nullable,        int length,        String name,        String dataType    ) {
        super(
        );
        this.scale = scale;
        this.default = default;
        this.nullable = nullable;
        this.length = length;
        this.name = name;
        this.dataType = dataType;
    }


    public int getScale() {
        return scale;
    }

    public void setScale(int scale) {
        this.scale = scale;
    }
    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }

    public core_TableDef getCore_tabledef() {
        return core_tabledef;
    }

    public void setCore_tabledef(core_TableDef core_tabledef) {
        this.core_tabledef = core_tabledef;
    }

}