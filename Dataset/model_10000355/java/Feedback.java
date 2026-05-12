





import java.util.List;
import java.util.ArrayList;

public class Feedback  {

    private int id;
    private String customername;
    private int phoneno;



    public Feedback(
        int id,        String customername,        int phoneno    ) {
        this.id = id;
        this.customername = customername;
        this.phoneno = phoneno;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getCustomername() {
        return customername;
    }

    public void setCustomername(String customername) {
        this.customername = customername;
    }
    public int getPhoneno() {
        return phoneno;
    }

    public void setPhoneno(int phoneno) {
        this.phoneno = phoneno;
    }


}