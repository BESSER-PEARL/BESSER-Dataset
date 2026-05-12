





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_CreateTriggerStatement extends DDLStatement {

    private boolean temporary;
    private String when;
    private String name;
    private String forEachRow;
    private String eventType;
    private String updateColumnNames;





    private sqliteModel_TableDefinition sqlitemodel_tabledefinition;


    public sqliteModel_CreateTriggerStatement(
        boolean temporary,        String when,        String name,        String forEachRow,        String eventType,        String updateColumnNames    ) {
        super(
        );
        this.temporary = temporary;
        this.when = when;
        this.name = name;
        this.forEachRow = forEachRow;
        this.eventType = eventType;
        this.updateColumnNames = updateColumnNames;
    }


    public boolean getTemporary() {
        return temporary;
    }

    public void setTemporary(boolean temporary) {
        this.temporary = temporary;
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
    public String getForeachrow() {
        return forEachRow;
    }

    public void setForeachrow(String forEachRow) {
        this.forEachRow = forEachRow;
    }
    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
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

}