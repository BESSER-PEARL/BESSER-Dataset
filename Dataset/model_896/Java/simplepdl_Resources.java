





import java.util.List;
import java.util.ArrayList;

public class simplepdl_Resources extends ProcessElement {

    private int quantite;
    private String name;



    public simplepdl_Resources(
        int quantite,        String name    ) {
        super(
        );
        this.quantite = quantite;
        this.name = name;
    }


    public int getQuantite() {
        return quantite;
    }

    public void setQuantite(int quantite) {
        this.quantite = quantite;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}