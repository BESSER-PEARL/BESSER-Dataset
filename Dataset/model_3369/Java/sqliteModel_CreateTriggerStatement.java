





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_CreateTriggerStatement extends DDLStatement {

    private String name;
    private String eventType;
    private String forEachRow;
    private String when;
    private boolean temporary;
    private String updateColumnNames;





    private sqliteModel_TableDefinition sqlitemodel_tabledefinition;




    private List<sqliteModel_DMLStatement> sqlitemodel_dmlstatements;




    private sqliteModel_Expression sqlitemodel_expression;




    private sqliteModel_DropTriggerStatement sqlitemodel_droptriggerstatement;


    public sqliteModel_CreateTriggerStatement(
        String name,        String eventType,        String forEachRow,        String when,        boolean temporary,        String updateColumnNames    ) {
        super(
        );
        this.name = name;
        this.eventType = eventType;
        this.forEachRow = forEachRow;
        this.when = when;
        this.temporary = temporary;
        this.updateColumnNames = updateColumnNames;
        this.sqlitemodel_dmlstatements = new ArrayList<>();
    }

    public sqliteModel_CreateTriggerStatement(
        String name,        String eventType,        String forEachRow,        String when,        boolean temporary,        String updateColumnNames        ArrayList<sqliteModel_DMLStatement> sqlitemodel_dmlstatements    ) {
        this.name = name;
        this.eventType = eventType;
        this.forEachRow = forEachRow;
        this.when = when;
        this.temporary = temporary;
        this.updateColumnNames = updateColumnNames;
        this.sqlitemodel_dmlstatements = sqlitemodel_dmlstatements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
    }
    public String getForeachrow() {
        return forEachRow;
    }

    public void setForeachrow(String forEachRow) {
        this.forEachRow = forEachRow;
    }
    public String getWhen() {
        return when;
    }

    public void setWhen(String when) {
        this.when = when;
    }
    public boolean getTemporary() {
        return temporary;
    }

    public void setTemporary(boolean temporary) {
        this.temporary = temporary;
    }
    public String getUpdatecolumnnames() {
        return updateColumnNames;
    }

    public void setUpdatecolumnnames(String updateColumnNames) {
        this.updateColumnNames = updateColumnNames;
    }

    public sqliteModel_TableDefinition getSqlitemodel_tabledefinition() {
        return sqlitemodel_tabledefinition;
    }

    public void setSqlitemodel_tabledefinition(sqliteModel_TableDefinition sqlitemodel_tabledefinition) {
        this.sqlitemodel_tabledefinition = sqlitemodel_tabledefinition;
    }
    public List<sqliteModel_DMLStatement> getSqlitemodel_dmlstatements() {
        return sqlitemodel_dmlstatements;
    }

    public void addSqlitemodel_dmlstatement(Sqlitemodel_dmlstatement sqlitemodel_dmlstatement) {
        this.sqlitemodel_dmlstatements.add(sqlitemodel_dmlstatement);
    }
    public sqliteModel_Expression getSqlitemodel_expression() {
        return sqlitemodel_expression;
    }

    public void setSqlitemodel_expression(sqliteModel_Expression sqlitemodel_expression) {
        this.sqlitemodel_expression = sqlitemodel_expression;
    }
    public sqliteModel_DropTriggerStatement getSqlitemodel_droptriggerstatement() {
        return sqlitemodel_droptriggerstatement;
    }

    public void setSqlitemodel_droptriggerstatement(sqliteModel_DropTriggerStatement sqlitemodel_droptriggerstatement) {
        this.sqlitemodel_droptriggerstatement = sqlitemodel_droptriggerstatement;
    }

}