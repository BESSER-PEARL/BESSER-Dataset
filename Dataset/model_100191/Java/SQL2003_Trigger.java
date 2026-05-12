





import java.util.List;
import java.util.ArrayList;

public class SQL2003_Trigger  {

    private String triggeredAction;
    private String event;
    private String actionTime;
    private String name;





    private List<SQL2003_StructuralComponent> sql2003_structuralcomponents;




    private SQL2003_Table sql2003_table;




    private SQL2003_Table sql2003_table;


    public SQL2003_Trigger(
        String triggeredAction,        String event,        String actionTime,        String name    ) {
        this.triggeredAction = triggeredAction;
        this.event = event;
        this.actionTime = actionTime;
        this.name = name;
        this.sql2003_structuralcomponents = new ArrayList<>();
    }

    public SQL2003_Trigger(
        String triggeredAction,        String event,        String actionTime,        String name        ArrayList<SQL2003_StructuralComponent> sql2003_structuralcomponents    ) {
        this.triggeredAction = triggeredAction;
        this.event = event;
        this.actionTime = actionTime;
        this.name = name;
        this.sql2003_structuralcomponents = sql2003_structuralcomponents;
    }

    public String getTriggeredaction() {
        return triggeredAction;
    }

    public void setTriggeredaction(String triggeredAction) {
        this.triggeredAction = triggeredAction;
    }
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }
    public String getActiontime() {
        return actionTime;
    }

    public void setActiontime(String actionTime) {
        this.actionTime = actionTime;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<SQL2003_StructuralComponent> getSql2003_structuralcomponents() {
        return sql2003_structuralcomponents;
    }

    public void addSql2003_structuralcomponent(Sql2003_structuralcomponent sql2003_structuralcomponent) {
        this.sql2003_structuralcomponents.add(sql2003_structuralcomponent);
    }
    public SQL2003_Table getSql2003_table() {
        return sql2003_table;
    }

    public void setSql2003_table(SQL2003_Table sql2003_table) {
        this.sql2003_table = sql2003_table;
    }
    public SQL2003_Table getSql2003_table() {
        return sql2003_table;
    }

    public void setSql2003_table(SQL2003_Table sql2003_table) {
        this.sql2003_table = sql2003_table;
    }

}