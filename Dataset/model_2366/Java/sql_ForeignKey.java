





import java.util.List;
import java.util.ArrayList;

public class sql_ForeignKey extends Key {






    private List<sql_Event> sql_events;




    private sql_Event sql_event;


    public sql_ForeignKey(
    ) {
        super(
        );
        this.sql_events = new ArrayList<>();
    }

    public sql_ForeignKey(
        ArrayList<sql_Event> sql_events    ) {
        this.sql_events = sql_events;
    }


    public List<sql_Event> getSql_events() {
        return sql_events;
    }

    public void addSql_event(Sql_event sql_event) {
        this.sql_events.add(sql_event);
    }
    public sql_Event getSql_event() {
        return sql_event;
    }

    public void setSql_event(sql_Event sql_event) {
        this.sql_event = sql_event;
    }

}