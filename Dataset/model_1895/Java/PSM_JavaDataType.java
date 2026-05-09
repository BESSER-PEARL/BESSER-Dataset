





import java.util.List;
import java.util.ArrayList;

public class PSM_JavaDataType extends JavaElement {

    private boolean IsPrimitive;
    private String JsonSchema;
    private String PackageName;



    public PSM_JavaDataType(
        boolean IsPrimitive,        String JsonSchema,        String PackageName    ) {
        super(
        );
        this.IsPrimitive = IsPrimitive;
        this.JsonSchema = JsonSchema;
        this.PackageName = PackageName;
    }


    public boolean getIsprimitive() {
        return IsPrimitive;
    }

    public void setIsprimitive(boolean IsPrimitive) {
        this.IsPrimitive = IsPrimitive;
    }
    public String getJsonschema() {
        return JsonSchema;
    }

    public void setJsonschema(String JsonSchema) {
        this.JsonSchema = JsonSchema;
    }
    public String getPackagename() {
        return PackageName;
    }

    public void setPackagename(String PackageName) {
        this.PackageName = PackageName;
    }


}