





import java.util.List;
import java.util.ArrayList;

public class connection_SalesforceModuleUnit extends AbstractMetadataObject {

    private String moduleName;



    public connection_SalesforceModuleUnit(
        String moduleName    ) {
        super(
        );
        this.moduleName = moduleName;
    }


    public String getModulename() {
        return moduleName;
    }

    public void setModulename(String moduleName) {
        this.moduleName = moduleName;
    }


}