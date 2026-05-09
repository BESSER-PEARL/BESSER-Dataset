





import java.util.List;
import java.util.ArrayList;

public class petrinetDsl_Storage  {

    private int capacity;
    private int count;





    private petrinetDsl_Resource petrinetdsl_resource;




    private petrinetDsl_Place petrinetdsl_place;


    public petrinetDsl_Storage(
        int capacity,        int count    ) {
        this.capacity = capacity;
        this.count = count;
    }


    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
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