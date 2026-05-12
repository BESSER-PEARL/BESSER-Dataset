





import java.util.List;
import java.util.ArrayList;

public class Feedback  {

    private int id;
    private int phoneno;
    private String customername;



    public Feedback(
        int id,        int phoneno,        String customername    ) {
        this.id = id;
        this.phoneno = phoneno;
        this.customername = customername;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
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


}