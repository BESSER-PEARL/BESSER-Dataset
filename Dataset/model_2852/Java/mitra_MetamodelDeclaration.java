





import java.util.List;
import java.util.ArrayList;

public class mitra_MetamodelDeclaration  {

    private String name;
    private String type;
    private String replaces;





    private mitra_ReferenceType mitra_referencetype;




    private mitra_Module mitra_module;


    public mitra_MetamodelDeclaration(
        String name,        String type,        String replaces    ) {
        this.name = name;
        this.type = type;
        this.replaces = replaces;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getReplaces() {
        return replaces;
    }

    public void setReplaces(String replaces) {
        this.replaces = replaces;
    }

    public mitra_ReferenceType getMitra_referencetype() {
        return mitra_referencetype;
    }

    public void setMitra_referencetype(mitra_ReferenceType mitra_referencetype) {
        this.mitra_referencetype = mitra_referencetype;
    }
    public mitra_Module getMitra_module() {
        return mitra_module;
    }

    public void setMitra_module(mitra_Module mitra_module) {
        this.mitra_module = mitra_module;
    }

}