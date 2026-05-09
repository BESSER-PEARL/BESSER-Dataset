





import java.util.List;
import java.util.ArrayList;

public class Sample_Book  {

    private String name;
    private String category;



    public Sample_Book(
        String name,        String category    ) {
        this.name = name;
        this.category = category;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }


}