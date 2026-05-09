





import java.util.List;
import java.util.ArrayList;

public class geneology_Member  {

    private boolean female;
    private String name;





    private geneology_Family geneology_family;




    private geneology_Family geneology_family;


    public geneology_Member(
        boolean female,        String name    ) {
        this.female = female;
        this.name = name;
    }


    public boolean getFemale() {
        return female;
    }

    public void setFemale(boolean female) {
        this.female = female;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public geneology_Family getGeneology_family() {
        return geneology_family;
    }

    public void setGeneology_family(geneology_Family geneology_family) {
        this.geneology_family = geneology_family;
    }
    public geneology_Family getGeneology_family() {
        return geneology_family;
    }

    public void setGeneology_family(geneology_Family geneology_family) {
        this.geneology_family = geneology_family;
    }

}