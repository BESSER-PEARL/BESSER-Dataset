





import java.util.List;
import java.util.ArrayList;

public class core_CatalogGenerationStrategy  {

    private boolean createIndexOnView;
    private boolean createRelativeRecordNumber;





    private core_CatalogContainer core_catalogcontainer;


    public core_CatalogGenerationStrategy(
        boolean createIndexOnView,        boolean createRelativeRecordNumber    ) {
        this.createIndexOnView = createIndexOnView;
        this.createRelativeRecordNumber = createRelativeRecordNumber;
    }


    public boolean getCreateindexonview() {
        return createIndexOnView;
    }

    public void setCreateindexonview(boolean createIndexOnView) {
        this.createIndexOnView = createIndexOnView;
    }
    public boolean getCreaterelativerecordnumber() {
        return createRelativeRecordNumber;
    }

    public void setCreaterelativerecordnumber(boolean createRelativeRecordNumber) {
        this.createRelativeRecordNumber = createRelativeRecordNumber;
    }

    public core_CatalogContainer getCore_catalogcontainer() {
        return core_catalogcontainer;
    }

    public void setCore_catalogcontainer(core_CatalogContainer core_catalogcontainer) {
        this.core_catalogcontainer = core_catalogcontainer;
    }

}