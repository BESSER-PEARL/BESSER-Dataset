





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_TableSpaceDefinition  {

    private boolean defaultSupported;
    private boolean extentSizeSupported;
    private int maximumIdentifierLength;
    private boolean containerInitialSizeSupported;
    private boolean typeSupported;
    private boolean managedBySupported;
    private boolean containerMaximumSizeSupported;
    private boolean containerExtentSizeSupported;
    private boolean pageSizeSupported;
    private String tableSpaceType;
    private boolean prefetchSizeSupported;
    private boolean bufferPoolSupported;





    private dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition;


    public dbdefinition_TableSpaceDefinition(
        boolean defaultSupported,        boolean extentSizeSupported,        int maximumIdentifierLength,        boolean containerInitialSizeSupported,        boolean typeSupported,        boolean managedBySupported,        boolean containerMaximumSizeSupported,        boolean containerExtentSizeSupported,        boolean pageSizeSupported,        String tableSpaceType,        boolean prefetchSizeSupported,        boolean bufferPoolSupported    ) {
        this.defaultSupported = defaultSupported;
        this.extentSizeSupported = extentSizeSupported;
        this.maximumIdentifierLength = maximumIdentifierLength;
        this.containerInitialSizeSupported = containerInitialSizeSupported;
        this.typeSupported = typeSupported;
        this.managedBySupported = managedBySupported;
        this.containerMaximumSizeSupported = containerMaximumSizeSupported;
        this.containerExtentSizeSupported = containerExtentSizeSupported;
        this.pageSizeSupported = pageSizeSupported;
        this.tableSpaceType = tableSpaceType;
        this.prefetchSizeSupported = prefetchSizeSupported;
        this.bufferPoolSupported = bufferPoolSupported;
    }


    public boolean getDefaultsupported() {
        return defaultSupported;
    }

    public void setDefaultsupported(boolean defaultSupported) {
        this.defaultSupported = defaultSupported;
    }
    public boolean getExtentsizesupported() {
        return extentSizeSupported;
    }

    public void setExtentsizesupported(boolean extentSizeSupported) {
        this.extentSizeSupported = extentSizeSupported;
    }
    public int getMaximumidentifierlength() {
        return maximumIdentifierLength;
    }

    public void setMaximumidentifierlength(int maximumIdentifierLength) {
        this.maximumIdentifierLength = maximumIdentifierLength;
    }
    public boolean getContainerinitialsizesupported() {
        return containerInitialSizeSupported;
    }

    public void setContainerinitialsizesupported(boolean containerInitialSizeSupported) {
        this.containerInitialSizeSupported = containerInitialSizeSupported;
    }
    public boolean getTypesupported() {
        return typeSupported;
    }

    public void setTypesupported(boolean typeSupported) {
        this.typeSupported = typeSupported;
    }
    public boolean getManagedbysupported() {
        return managedBySupported;
    }

    public void setManagedbysupported(boolean managedBySupported) {
        this.managedBySupported = managedBySupported;
    }
    public boolean getContainermaximumsizesupported() {
        return containerMaximumSizeSupported;
    }

    public void setContainermaximumsizesupported(boolean containerMaximumSizeSupported) {
        this.containerMaximumSizeSupported = containerMaximumSizeSupported;
    }
    public boolean getContainerextentsizesupported() {
        return containerExtentSizeSupported;
    }

    public void setContainerextentsizesupported(boolean containerExtentSizeSupported) {
        this.containerExtentSizeSupported = containerExtentSizeSupported;
    }
    public boolean getPagesizesupported() {
        return pageSizeSupported;
    }

    public void setPagesizesupported(boolean pageSizeSupported) {
        this.pageSizeSupported = pageSizeSupported;
    }
    public String getTablespacetype() {
        return tableSpaceType;
    }

    public void setTablespacetype(String tableSpaceType) {
        this.tableSpaceType = tableSpaceType;
    }
    public boolean getPrefetchsizesupported() {
        return prefetchSizeSupported;
    }

    public void setPrefetchsizesupported(boolean prefetchSizeSupported) {
        this.prefetchSizeSupported = prefetchSizeSupported;
    }
    public boolean getBufferpoolsupported() {
        return bufferPoolSupported;
    }

    public void setBufferpoolsupported(boolean bufferPoolSupported) {
        this.bufferPoolSupported = bufferPoolSupported;
    }

    public dbdefinition_DatabaseVendorDefinition getDbdefinition_databasevendordefinition() {
        return dbdefinition_databasevendordefinition;
    }

    public void setDbdefinition_databasevendordefinition(dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition) {
        this.dbdefinition_databasevendordefinition = dbdefinition_databasevendordefinition;
    }

}