





import java.util.List;
import java.util.ArrayList;

public class Feedback  {

    private int phoneno;
    private String customername;
    private int id;



    public Feedback(
        int phoneno,        String customername,        int id    ) {
        this.phoneno = phoneno;
        this.customername = customername;
        this.id = id;
    }


    public int getPhoneno() {
        return phoneno;
    }

    public void setPhoneno(int phoneno) {
        this.phoneno = phoneno;
    }
    public String getCustomername() {
        return customername;
    }

    public void setCustomername(String customername) {
        this.customername = customername;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}