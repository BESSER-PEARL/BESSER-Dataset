





import java.util.List;
import java.util.ArrayList;

public class Librarian  {

    private int id;
    private String attribute;
    private String password;





    private log log;


    public Librarian(
        int id,        String attribute,        String password    ) {
        this.id = id;
        this.attribute = attribute;
        this.password = password;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public log getLog() {
        return log;
    }

    public void setLog(log log) {
        this.log = log;
    }

}