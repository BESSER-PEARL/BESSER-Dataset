





import java.util.List;
import java.util.ArrayList;

public class core_TableColumnDef extends DatabaseObjectDef {

    private String name;
    private boolean default;
    private boolean nullable;





    private core_TableDef core_tabledef;


    public core_TableColumnDef(
        String name,        boolean default,        boolean nullable    ) {
        super(
        );
        this.name = name;
        this.default = default;
        this.nullable = nullable;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

    public core_TableDef getCore_tabledef() {
        return core_tabledef;
    }

    public void setCore_tabledef(core_TableDef core_tabledef) {
        this.core_tabledef = core_tabledef;
    }

}