





import java.util.List;
import java.util.ArrayList;

public class simplepdl_Ressource extends ProcessElement {

    private int occurence;
    private String name;



    public simplepdl_Ressource(
        int occurence,        String name    ) {
        super(
        );
        this.occurence = occurence;
        this.name = name;
    }


    public int getOccurence() {
        return occurence;
    }

    public void setOccurence(int occurence) {
        this.occurence = occurence;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}