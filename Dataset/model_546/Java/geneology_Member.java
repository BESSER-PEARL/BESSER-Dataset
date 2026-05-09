





import java.util.List;
import java.util.ArrayList;

public class geneology_Member  {

    private String name;
    private boolean female;





    private geneology_Family geneology_family;




    private geneology_Family geneology_family;


    public geneology_Member(
        String name,        boolean female    ) {
        this.name = name;
        this.female = female;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getFemale() {
        return female;
    }

    public void setFemale(boolean female) {
        this.female = female;
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