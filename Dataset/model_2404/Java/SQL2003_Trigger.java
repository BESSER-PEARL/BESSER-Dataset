





import java.util.List;
import java.util.ArrayList;

public class SQL2003_Trigger  {

    private String actionTime;
    private String triggeredAction;
    private String name;
    private String event;





    private SQL2003_Table sql2003_table;




    private SQL2003_Table sql2003_table;




    private List<SQL2003_StructuralComponent> sql2003_structuralcomponents;


    public SQL2003_Trigger(
        String actionTime,        String triggeredAction,        String name,        String event    ) {
        this.actionTime = actionTime;
        this.triggeredAction = triggeredAction;
        this.name = name;
        this.event = event;
        this.sql2003_structuralcomponents = new ArrayList<>();
    }

    public SQL2003_Trigger(
        String actionTime,        String triggeredAction,        String name,        String event        ArrayList<SQL2003_StructuralComponent> sql2003_structuralcomponents    ) {
        this.actionTime = actionTime;
        this.triggeredAction = triggeredAction;
        this.name = name;
        this.event = event;
        this.sql2003_structuralcomponents = sql2003_structuralcomponents;
    }

    public String getActiontime() {
        return actionTime;
    }

    public void setActiontime(String actionTime) {
        this.actionTime = actionTime;
    }
    public String getTriggeredaction() {
        return triggeredAction;
    }

    public void setTriggeredaction(String triggeredAction) {
        this.triggeredAction = triggeredAction;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
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
    public List<SQL2003_StructuralComponent> getSql2003_structuralcomponents() {
        return sql2003_structuralcomponents;
    }

    public void addSql2003_structuralcomponent(Sql2003_structuralcomponent sql2003_structuralcomponent) {
        this.sql2003_structuralcomponents.add(sql2003_structuralcomponent);
    }

}