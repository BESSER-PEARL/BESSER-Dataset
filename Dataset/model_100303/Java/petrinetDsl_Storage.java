





import java.util.List;
import java.util.ArrayList;

public class petrinetDsl_Storage  {

    private int count;
    private int capacity;





    private petrinetDsl_Resource petrinetdsl_resource;




    private petrinetDsl_Place petrinetdsl_place;


    public petrinetDsl_Storage(
        int count,        int capacity    ) {
        this.count = count;
        this.capacity = capacity;
    }


    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public petrinetDsl_Resource getPetrinetdsl_resource() {
        return petrinetdsl_resource;
    }

    public void setPetrinetdsl_resource(petrinetDsl_Resource petrinetdsl_resource) {
        this.petrinetdsl_resource = petrinetdsl_resource;
    }
    public petrinetDsl_Place getPetrinetdsl_place() {
        return petrinetdsl_place;
    }

    public void setPetrinetdsl_place(petrinetDsl_Place petrinetdsl_place) {
        this.petrinetdsl_place = petrinetdsl_place;
    }

}