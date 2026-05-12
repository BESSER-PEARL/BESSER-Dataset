





import java.util.List;
import java.util.ArrayList;

public class TimeInterval  {

    private String date;
    private int weekIdentifier;
    private int id;
    private int classOrder;
    private int weekday;



    public TimeInterval(
        String date,        int weekIdentifier,        int id,        int classOrder,        int weekday    ) {
        this.date = date;
        this.weekIdentifier = weekIdentifier;
        this.id = id;
        this.classOrder = classOrder;
        this.weekday = weekday;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public int getWeekidentifier() {
        return weekIdentifier;
    }

    public void setWeekidentifier(int weekIdentifier) {
        this.weekIdentifier = weekIdentifier;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getClassorder() {
        return classOrder;
    }

    public void setClassorder(int classOrder) {
        this.classOrder = classOrder;
    }
    public int getWeekday() {
        return weekday;
    }

    public void setWeekday(int weekday) {
        this.weekday = weekday;
    }


}