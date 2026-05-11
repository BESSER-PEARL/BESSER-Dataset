





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_CreateTriggerStatement extends DDLStatement {

    private boolean temporary;
    private String updateColumnNames;
    private String forEachRow;
    private String when;
    private String name;
    private String eventType;





    private sqliteModel_TableDefinition sqlitemodel_tabledefinition;




    private sqliteModel_DropTriggerStatement sqlitemodel_droptriggerstatement;




    private sqliteModel_Expression sqlitemodel_expression;


    public sqliteModel_CreateTriggerStatement(
        boolean temporary,        String updateColumnNames,        String forEachRow,        String when,        String name,        String eventType    ) {
        super(
        );
        this.temporary = temporary;
        this.updateColumnNames = updateColumnNames;
        this.forEachRow = forEachRow;
        this.when = when;
        this.name = name;
        this.eventType = eventType;
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

    public sqliteModel_TableDefinition getSqlitemodel_tabledefinition() {
        return sqlitemodel_tabledefinition;
    }

    public void setSqlitemodel_tabledefinition(sqliteModel_TableDefinition sqlitemodel_tabledefinition) {
        this.sqlitemodel_tabledefinition = sqlitemodel_tabledefinition;
    }
    public sqliteModel_DropTriggerStatement getSqlitemodel_droptriggerstatement() {
        return sqlitemodel_droptriggerstatement;
    }

    public void setSqlitemodel_droptriggerstatement(sqliteModel_DropTriggerStatement sqlitemodel_droptriggerstatement) {
        this.sqlitemodel_droptriggerstatement = sqlitemodel_droptriggerstatement;
    }
    public sqliteModel_Expression getSqlitemodel_expression() {
        return sqlitemodel_expression;
    }

    public void setSqlitemodel_expression(sqliteModel_Expression sqlitemodel_expression) {
        this.sqlitemodel_expression = sqlitemodel_expression;
    }

}