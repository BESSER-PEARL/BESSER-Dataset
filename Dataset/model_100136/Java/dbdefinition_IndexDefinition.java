





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_IndexDefinition  {

    private boolean clusterChangeable;
    private boolean clusteringSupported;
    private int maximumIdentifierLength;
    private boolean fillFactorSupported;
    private boolean percentFreeChangeable;
    private boolean includedColumnsSupported;
    private String percentFreeTerminology;





    private dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition;


    public dbdefinition_IndexDefinition(
        boolean clusterChangeable,        boolean clusteringSupported,        int maximumIdentifierLength,        boolean fillFactorSupported,        boolean percentFreeChangeable,        boolean includedColumnsSupported,        String percentFreeTerminology    ) {
        this.clusterChangeable = clusterChangeable;
        this.clusteringSupported = clusteringSupported;
        this.maximumIdentifierLength = maximumIdentifierLength;
        this.fillFactorSupported = fillFactorSupported;
        this.percentFreeChangeable = percentFreeChangeable;
        this.includedColumnsSupported = includedColumnsSupported;
        this.percentFreeTerminology = percentFreeTerminology;
    }


    public boolean getClusterchangeable() {
        return clusterChangeable;
    }

    public void setClusterchangeable(boolean clusterChangeable) {
        this.clusterChangeable = clusterChangeable;
    }
    public boolean getClusteringsupported() {
        return clusteringSupported;
    }

    public void setClusteringsupported(boolean clusteringSupported) {
        this.clusteringSupported = clusteringSupported;
    }
    public int getMaximumidentifierlength() {
        return maximumIdentifierLength;
    }

    public void setMaximumidentifierlength(int maximumIdentifierLength) {
        this.maximumIdentifierLength = maximumIdentifierLength;
    }
    public boolean getFillfactorsupported() {
        return fillFactorSupported;
    }

    public void setFillfactorsupported(boolean fillFactorSupported) {
        this.fillFactorSupported = fillFactorSupported;
    }
    public boolean getPercentfreechangeable() {
        return percentFreeChangeable;
    }

    public void setPercentfreechangeable(boolean percentFreeChangeable) {
        this.percentFreeChangeable = percentFreeChangeable;
    }
    public boolean getIncludedcolumnssupported() {
        return includedColumnsSupported;
    }

    public void setIncludedcolumnssupported(boolean includedColumnsSupported) {
        this.includedColumnsSupported = includedColumnsSupported;
    }
    public String getPercentfreeterminology() {
        return percentFreeTerminology;
    }

    public void setPercentfreeterminology(String percentFreeTerminology) {
        this.percentFreeTerminology = percentFreeTerminology;
    }

    public dbdefinition_DatabaseVendorDefinition getDbdefinition_databasevendordefinition() {
        return dbdefinition_databasevendordefinition;
    }

    public void setDbdefinition_databasevendordefinition(dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition) {
        this.dbdefinition_databasevendordefinition = dbdefinition_databasevendordefinition;
    }

}