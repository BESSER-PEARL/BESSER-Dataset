





import java.util.List;
import java.util.ArrayList;

public class company_Company  {

    private String name;
    private String size;



    public company_Company(
        String name,        String size    ) {
        this.name = name;
        this.size = size;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }


}