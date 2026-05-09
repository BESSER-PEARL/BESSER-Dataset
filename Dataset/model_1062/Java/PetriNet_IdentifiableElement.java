





import java.util.List;
import java.util.ArrayList;

public class PetriNet_IdentifiableElement  {

    private String name;
    private String author;



    public PetriNet_IdentifiableElement(
        String name,        String author    ) {
        this.name = name;
        this.author = author;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }


}