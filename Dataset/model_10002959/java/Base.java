





import java.util.List;
import java.util.ArrayList;

public class Base  {

    private String name;
    private boolean isVegetarian;



    public Base(
        String name,        boolean isVegetarian    ) {
        this.name = name;
        this.isVegetarian = isVegetarian;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsvegetarian() {
        return isVegetarian;
    }

    public void setIsvegetarian(boolean isVegetarian) {
        this.isVegetarian = isVegetarian;
    }


}