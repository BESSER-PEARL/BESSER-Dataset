





import java.util.List;
import java.util.ArrayList;

public class bean_ProfileInfo  {

    private String first;
    private String email;
    private String path;
    private String last;



    public bean_ProfileInfo(
        String first,        String email,        String path,        String last    ) {
        this.first = first;
        this.email = email;
        this.path = path;
        this.last = last;
    }


    public String getFirst() {
        return first;
    }

    public void setFirst(String first) {
        this.first = first;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getLast() {
        return last;
    }

    public void setLast(String last) {
        this.last = last;
    }


}