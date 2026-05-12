





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_CreateTriggerStatement extends DDLStatement {

    private String eventType;
    private String when;
    private String forEachRow;
    private String name;
    private String updateColumnNames;
    private boolean temporary;





    private sqliteModel_TableDefinition sqlitemodel_tabledefinition;




    private sqliteModel_Expression sqlitemodel_expression;


    public sqliteModel_CreateTriggerStatement(
        String eventType,        String when,        String forEachRow,        String name,        String updateColumnNames,        boolean temporary    ) {
        super(
        );
        this.eventType = eventType;
        this.when = when;
        this.forEachRow = forEachRow;
        this.name = name;
        this.updateColumnNames = updateColumnNames;
        this.temporary = temporary;
    }


    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
    }
    public String getWhen() {
        return when;
    }

    public void setWhen(String when) {
        this.when = when;
    }
    public String getForeachrow() {
        return forEachRow;
    }

    public void setForeachrow(String forEachRow) {
        this.forEachRow = forEachRow;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUpdatecolumnnames() {
        return updateColumnNames;
    }

    public void setUpdatecolumnnames(String updateColumnNames) {
        this.updateColumnNames = updateColumnNames;
    }
    public boolean getTemporary() {
        return temporary;
    }

    public void setTemporary(boolean temporary) {
        this.temporary = temporary;
    }

    public sqliteModel_TableDefinition getSqlitemodel_tabledefinition() {
        return sqlitemodel_tabledefinition;
    }

    public void setSqlitemodel_tabledefinition(sqliteModel_TableDefinition sqlitemodel_tabledefinition) {
        this.sqlitemodel_tabledefinition = sqlitemodel_tabledefinition;
    }
    public sqliteModel_Expression getSqlitemodel_expression() {
        return sqlitemodel_expression;
    }

    public void setSqlitemodel_expression(sqliteModel_Expression sqlitemodel_expression) {
        this.sqlitemodel_expression = sqlitemodel_expression;
    }

}