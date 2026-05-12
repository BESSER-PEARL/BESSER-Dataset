





import java.util.List;
import java.util.ArrayList;

public class Item  {

    private int maxCheckOut;
    private int age;





    private Library library;


    public Item(
        int maxCheckOut,        int age    ) {
        this.maxCheckOut = maxCheckOut;
        this.age = age;
    }


    public int getMaxcheckout() {
        return maxCheckOut;
    }

    public void setMaxcheckout(int maxCheckOut) {
        this.maxCheckOut = maxCheckOut;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public Library getLibrary() {
        return library;
    }

    public void setLibrary(Library library) {
        this.library = library;
    }

}