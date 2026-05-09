





import java.util.List;
import java.util.ArrayList;

public class simplepdl_Parameter extends ProcessElement {

    private String name;
    private int nbNeeds;



    public simplepdl_Parameter(
        String name,        int nbNeeds    ) {
        super(
        );
        this.name = name;
        this.nbNeeds = nbNeeds;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getNbneeds() {
        return nbNeeds;
    }

    public void setNbneeds(int nbNeeds) {
        this.nbNeeds = nbNeeds;
    }


}