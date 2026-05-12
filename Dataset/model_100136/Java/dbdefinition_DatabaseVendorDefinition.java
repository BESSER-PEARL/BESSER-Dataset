





import java.util.List;
import java.util.ArrayList;

public class dbdefinition_DatabaseVendorDefinition  {

    private boolean quotedDDLSupported;
    private boolean roleSupported;
    private String version;
    private boolean tablespacesSupported;
    private boolean userDefinedTypeSupported;
    private boolean sqlUDFSupported;
    private String vendor;
    private boolean userSupported;
    private boolean sequenceSupported;
    private boolean triggerSupported;
    private boolean joinSupported;
    private boolean constraintsSupported;
    private boolean uDFSupported;
    private boolean snapshotViewSupported;
    private boolean domainSupported;
    private int maximumCommentLength;
    private boolean nicknameSupported;
    private boolean mQTSupported;
    private boolean viewTriggerSupported;
    private boolean SQLStatementSupported;
    private boolean storedProcedureSupported;
    private boolean schemaSupported;
    private int maximumIdentifierLength;
    private boolean constructedDataTypeSupported;
    private boolean eventSupported;
    private boolean groupSupported;
    private boolean mQTIndexSupported;
    private boolean packageSupported;
    private boolean quotedDMLSupported;
    private boolean synonymSupported;
    private boolean aliasSupported;
    private boolean xmlSupported;
    private boolean roleAuthorizationSupported;
    private boolean authorizationIdentifierSupported;



    public dbdefinition_DatabaseVendorDefinition(
        boolean quotedDDLSupported,        boolean roleSupported,        String version,        boolean tablespacesSupported,        boolean userDefinedTypeSupported,        boolean sqlUDFSupported,        String vendor,        boolean userSupported,        boolean sequenceSupported,        boolean triggerSupported,        boolean joinSupported,        boolean constraintsSupported,        boolean uDFSupported,        boolean snapshotViewSupported,        boolean domainSupported,        int maximumCommentLength,        boolean nicknameSupported,        boolean mQTSupported,        boolean viewTriggerSupported,        boolean SQLStatementSupported,        boolean storedProcedureSupported,        boolean schemaSupported,        int maximumIdentifierLength,        boolean constructedDataTypeSupported,        boolean eventSupported,        boolean groupSupported,        boolean mQTIndexSupported,        boolean packageSupported,        boolean quotedDMLSupported,        boolean synonymSupported,        boolean aliasSupported,        boolean xmlSupported,        boolean roleAuthorizationSupported,        boolean authorizationIdentifierSupported    ) {
        this.quotedDDLSupported = quotedDDLSupported;
        this.roleSupported = roleSupported;
        this.version = version;
        this.tablespacesSupported = tablespacesSupported;
        this.userDefinedTypeSupported = userDefinedTypeSupported;
        this.sqlUDFSupported = sqlUDFSupported;
        this.vendor = vendor;
        this.userSupported = userSupported;
        this.sequenceSupported = sequenceSupported;
        this.triggerSupported = triggerSupported;
        this.joinSupported = joinSupported;
        this.constraintsSupported = constraintsSupported;
        this.uDFSupported = uDFSupported;
        this.snapshotViewSupported = snapshotViewSupported;
        this.domainSupported = domainSupported;
        this.maximumCommentLength = maximumCommentLength;
        this.nicknameSupported = nicknameSupported;
        this.mQTSupported = mQTSupported;
        this.viewTriggerSupported = viewTriggerSupported;
        this.SQLStatementSupported = SQLStatementSupported;
        this.storedProcedureSupported = storedProcedureSupported;
        this.schemaSupported = schemaSupported;
        this.maximumIdentifierLength = maximumIdentifierLength;
        this.constructedDataTypeSupported = constructedDataTypeSupported;
        this.eventSupported = eventSupported;
        this.groupSupported = groupSupported;
        this.mQTIndexSupported = mQTIndexSupported;
        this.packageSupported = packageSupported;
        this.quotedDMLSupported = quotedDMLSupported;
        this.synonymSupported = synonymSupported;
        this.aliasSupported = aliasSupported;
        this.xmlSupported = xmlSupported;
        this.roleAuthorizationSupported = roleAuthorizationSupported;
        this.authorizationIdentifierSupported = authorizationIdentifierSupported;
    }


    public boolean getQuotedddlsupported() {
        return quotedDDLSupported;
    }

    public void setQuotedddlsupported(boolean quotedDDLSupported) {
        this.quotedDDLSupported = quotedDDLSupported;
    }
    public boolean getRolesupported() {
        return roleSupported;
    }

    public void setRolesupported(boolean roleSupported) {
        this.roleSupported = roleSupported;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public boolean getTablespacessupported() {
        return tablespacesSupported;
    }

    public void setTablespacessupported(boolean tablespacesSupported) {
        this.tablespacesSupported = tablespacesSupported;
    }
    public boolean getUserdefinedtypesupported() {
        return userDefinedTypeSupported;
    }

    public void setUserdefinedtypesupported(boolean userDefinedTypeSupported) {
        this.userDefinedTypeSupported = userDefinedTypeSupported;
    }
    public boolean getSqludfsupported() {
        return sqlUDFSupported;
    }

    public void setSqludfsupported(boolean sqlUDFSupported) {
        this.sqlUDFSupported = sqlUDFSupported;
    }
    public String getVendor() {
        return vendor;
    }

    public void setVendor(String vendor) {
        this.vendor = vendor;
    }
    public boolean getUsersupported() {
        return userSupported;
    }

    public void setUsersupported(boolean userSupported) {
        this.userSupported = userSupported;
    }
    public boolean getSequencesupported() {
        return sequenceSupported;
    }

    public void setSequencesupported(boolean sequenceSupported) {
        this.sequenceSupported = sequenceSupported;
    }
    public boolean getTriggersupported() {
        return triggerSupported;
    }

    public void setTriggersupported(boolean triggerSupported) {
        this.triggerSupported = triggerSupported;
    }
    public boolean getJoinsupported() {
        return joinSupported;
    }

    public void setJoinsupported(boolean joinSupported) {
        this.joinSupported = joinSupported;
    }
    public boolean getConstraintssupported() {
        return constraintsSupported;
    }

    public void setConstraintssupported(boolean constraintsSupported) {
        this.constraintsSupported = constraintsSupported;
    }
    public boolean getUdfsupported() {
        return uDFSupported;
    }

    public void setUdfsupported(boolean uDFSupported) {
        this.uDFSupported = uDFSupported;
    }
    public boolean getSnapshotviewsupported() {
        return snapshotViewSupported;
    }

    public void setSnapshotviewsupported(boolean snapshotViewSupported) {
        this.snapshotViewSupported = snapshotViewSupported;
    }
    public boolean getDomainsupported() {
        return domainSupported;
    }

    public void setDomainsupported(boolean domainSupported) {
        this.domainSupported = domainSupported;
    }
    public int getMaximumcommentlength() {
        return maximumCommentLength;
    }

    public void setMaximumcommentlength(int maximumCommentLength) {
        this.maximumCommentLength = maximumCommentLength;
    }
    public boolean getNicknamesupported() {
        return nicknameSupported;
    }

    public void setNicknamesupported(boolean nicknameSupported) {
        this.nicknameSupported = nicknameSupported;
    }
    public boolean getMqtsupported() {
        return mQTSupported;
    }

    public void setMqtsupported(boolean mQTSupported) {
        this.mQTSupported = mQTSupported;
    }
    public boolean getViewtriggersupported() {
        return viewTriggerSupported;
    }

    public void setViewtriggersupported(boolean viewTriggerSupported) {
        this.viewTriggerSupported = viewTriggerSupported;
    }
    public boolean getSqlstatementsupported() {
        return SQLStatementSupported;
    }

    public void setSqlstatementsupported(boolean SQLStatementSupported) {
        this.SQLStatementSupported = SQLStatementSupported;
    }
    public boolean getStoredproceduresupported() {
        return storedProcedureSupported;
    }

    public void setStoredproceduresupported(boolean storedProcedureSupported) {
        this.storedProcedureSupported = storedProcedureSupported;
    }
    public boolean getSchemasupported() {
        return schemaSupported;
    }

    public void setSchemasupported(boolean schemaSupported) {
        this.schemaSupported = schemaSupported;
    }
    public int getMaximumidentifierlength() {
        return maximumIdentifierLength;
    }

    public void setMaximumidentifierlength(int maximumIdentifierLength) {
        this.maximumIdentifierLength = maximumIdentifierLength;
    }
    public boolean getConstructeddatatypesupported() {
        return constructedDataTypeSupported;
    }

    public void setConstructeddatatypesupported(boolean constructedDataTypeSupported) {
        this.constructedDataTypeSupported = constructedDataTypeSupported;
    }
    public boolean getEventsupported() {
        return eventSupported;
    }

    public void setEventsupported(boolean eventSupported) {
        this.eventSupported = eventSupported;
    }
    public boolean getGroupsupported() {
        return groupSupported;
    }

    public void setGroupsupported(boolean groupSupported) {
        this.groupSupported = groupSupported;
    }
    public boolean getMqtindexsupported() {
        return mQTIndexSupported;
    }

    public void setMqtindexsupported(boolean mQTIndexSupported) {
        this.mQTIndexSupported = mQTIndexSupported;
    }
    public boolean getPackagesupported() {
        return packageSupported;
    }

    public void setPackagesupported(boolean packageSupported) {
        this.packageSupported = packageSupported;
    }
    public boolean getQuoteddmlsupported() {
        return quotedDMLSupported;
    }

    public void setQuoteddmlsupported(boolean quotedDMLSupported) {
        this.quotedDMLSupported = quotedDMLSupported;
    }
    public boolean getSynonymsupported() {
        return synonymSupported;
    }

    public void setSynonymsupported(boolean synonymSupported) {
        this.synonymSupported = synonymSupported;
    }
    public boolean getAliassupported() {
        return aliasSupported;
    }

    public void setAliassupported(boolean aliasSupported) {
        this.aliasSupported = aliasSupported;
    }
    public boolean getXmlsupported() {
        return xmlSupported;
    }

    public void setXmlsupported(boolean xmlSupported) {
        this.xmlSupported = xmlSupported;
    }
    public boolean getRoleauthorizationsupported() {
        return roleAuthorizationSupported;
    }

    public void setRoleauthorizationsupported(boolean roleAuthorizationSupported) {
        this.roleAuthorizationSupported = roleAuthorizationSupported;
    }
    public boolean getAuthorizationidentifiersupported() {
        return authorizationIdentifierSupported;
    }

    public void setAuthorizationidentifiersupported(boolean authorizationIdentifierSupported) {
        this.authorizationIdentifierSupported = authorizationIdentifierSupported;
    }


}