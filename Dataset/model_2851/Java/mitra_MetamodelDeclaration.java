





import java.util.List;
import java.util.ArrayList;

public class mitra_MetamodelDeclaration  {

    private String type;
    private String name;
    private String replaces;





    private mitra_Module mitra_module;


    public mitra_MetamodelDeclaration(
        String type,        String name,        String replaces    ) {
        this.type = type;
        this.name = name;
        this.replaces = replaces;
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
    public String getReplaces() {
        return replaces;
    }

    public void setReplaces(String replaces) {
        this.replaces = replaces;
    }

    public mitra_Module getMitra_module() {
        return mitra_module;
    }

    public void setMitra_module(mitra_Module mitra_module) {
        this.mitra_module = mitra_module;
    }

}