





import java.util.List;
import java.util.ArrayList;

public class Fashion  {

    private int increaseBy;
    private String category;
    private None size;



    public Fashion(
        int increaseBy,        String category,        None size    ) {
        this.increaseBy = increaseBy;
        this.category = category;
        this.size = size;
    }


    public int getIncreaseby() {
        return increaseBy;
    }

    public void setIncreaseby(int increaseBy) {
        this.increaseBy = increaseBy;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public None getSize() {
        return size;
    }

    public void setSize(None size) {
        this.size = size;
    }


}