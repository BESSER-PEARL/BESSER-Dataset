





import java.util.List;
import java.util.ArrayList;

public class nupn_NUPNToolspecificType  {

    private String tool;
    private String mixed;
    private String version;





    private nupn_SizeType nupn_sizetype;




    private nupn_StructureType nupn_structuretype;


    public nupn_NUPNToolspecificType(
        String tool,        String mixed,        String version    ) {
        this.tool = tool;
        this.mixed = mixed;
        this.version = version;
    }


    public String getTool() {
        return tool;
    }

    public void setTool(String tool) {
        this.tool = tool;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public nupn_SizeType getNupn_sizetype() {
        return nupn_sizetype;
    }

    public void setNupn_sizetype(nupn_SizeType nupn_sizetype) {
        this.nupn_sizetype = nupn_sizetype;
    }
    public nupn_StructureType getNupn_structuretype() {
        return nupn_structuretype;
    }

    public void setNupn_structuretype(nupn_StructureType nupn_structuretype) {
        this.nupn_structuretype = nupn_structuretype;
    }

}