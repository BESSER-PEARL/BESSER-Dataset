





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_QueryDefinition  {

    private boolean tableAliasInDeleteSupported;
    private boolean castExpressionSupported;
    private boolean extendedGroupingSupported;
    private String identifierQuoteString;
    private String hostVariableMarker;
    private boolean defaultKeywordForInsertValueSupported;
    private boolean hostVariableMarkerSupported;





    private dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition;


    public dbdefinition_QueryDefinition(
        boolean tableAliasInDeleteSupported,        boolean castExpressionSupported,        boolean extendedGroupingSupported,        String identifierQuoteString,        String hostVariableMarker,        boolean defaultKeywordForInsertValueSupported,        boolean hostVariableMarkerSupported    ) {
        this.tableAliasInDeleteSupported = tableAliasInDeleteSupported;
        this.castExpressionSupported = castExpressionSupported;
        this.extendedGroupingSupported = extendedGroupingSupported;
        this.identifierQuoteString = identifierQuoteString;
        this.hostVariableMarker = hostVariableMarker;
        this.defaultKeywordForInsertValueSupported = defaultKeywordForInsertValueSupported;
        this.hostVariableMarkerSupported = hostVariableMarkerSupported;
    }


    public boolean getTablealiasindeletesupported() {
        return tableAliasInDeleteSupported;
    }

    public void setTablealiasindeletesupported(boolean tableAliasInDeleteSupported) {
        this.tableAliasInDeleteSupported = tableAliasInDeleteSupported;
    }
    public boolean getCastexpressionsupported() {
        return castExpressionSupported;
    }

    public void setCastexpressionsupported(boolean castExpressionSupported) {
        this.castExpressionSupported = castExpressionSupported;
    }
    public boolean getExtendedgroupingsupported() {
        return extendedGroupingSupported;
    }

    public void setExtendedgroupingsupported(boolean extendedGroupingSupported) {
        this.extendedGroupingSupported = extendedGroupingSupported;
    }
    public String getIdentifierquotestring() {
        return identifierQuoteString;
    }

    public void setIdentifierquotestring(String identifierQuoteString) {
        this.identifierQuoteString = identifierQuoteString;
    }
    public String getHostvariablemarker() {
        return hostVariableMarker;
    }

    public void setHostvariablemarker(String hostVariableMarker) {
        this.hostVariableMarker = hostVariableMarker;
    }
    public boolean getDefaultkeywordforinsertvaluesupported() {
        return defaultKeywordForInsertValueSupported;
    }

    public void setDefaultkeywordforinsertvaluesupported(boolean defaultKeywordForInsertValueSupported) {
        this.defaultKeywordForInsertValueSupported = defaultKeywordForInsertValueSupported;
    }
    public boolean getHostvariablemarkersupported() {
        return hostVariableMarkerSupported;
    }

    public void setHostvariablemarkersupported(boolean hostVariableMarkerSupported) {
        this.hostVariableMarkerSupported = hostVariableMarkerSupported;
    }

    public dbdefinition_DatabaseVendorDefinition getDbdefinition_databasevendordefinition() {
        return dbdefinition_databasevendordefinition;
    }

    public void setDbdefinition_databasevendordefinition(dbdefinition_DatabaseVendorDefinition dbdefinition_databasevendordefinition) {
        this.dbdefinition_databasevendordefinition = dbdefinition_databasevendordefinition;
    }

}