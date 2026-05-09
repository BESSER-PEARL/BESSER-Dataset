





import java.util.List;
import java.util.ArrayList;

public class Classes_Statistics_StatisticEntry  {

    private String value;





    private Date date;


    public Classes_Statistics_StatisticEntry(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

}