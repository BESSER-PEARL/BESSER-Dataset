





import java.util.List;
import java.util.ArrayList;

public class model3_File  {

    private String data;
    private String name;



    public model3_File(
        String data,        String name    ) {
        this.data = data;
        this.name = name;
    }


    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}