





import java.util.List;
import java.util.ArrayList;

public class company_Company  {

    private String size;
    private String name;



    public company_Company(
        String size,        String name    ) {
        this.size = size;
        this.name = name;
    }


    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}