





import java.util.List;
import java.util.ArrayList;

public class Events  {

    private int id;
    private String user;
    private int datetime;
    private String name;



    public Events(
        int id,        String user,        int datetime,        String name    ) {
        this.id = id;
        this.user = user;
        this.datetime = datetime;
        this.name = name;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }
    public int getDatetime() {
        return datetime;
    }

    public void setDatetime(int datetime) {
        this.datetime = datetime;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}