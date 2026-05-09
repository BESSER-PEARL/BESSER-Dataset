





import java.util.List;
import java.util.ArrayList;

public class OCLinEmig_Module  {

    private String name;





    private List<OCLinEmig_OclFeatureDefinition> oclinemig_oclfeaturedefinitions;


    public OCLinEmig_Module(
        String name    ) {
        this.name = name;
        this.oclinemig_oclfeaturedefinitions = new ArrayList<>();
    }

    public OCLinEmig_Module(
        String name        ArrayList<OCLinEmig_OclFeatureDefinition> oclinemig_oclfeaturedefinitions    ) {
        this.name = name;
        this.oclinemig_oclfeaturedefinitions = oclinemig_oclfeaturedefinitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<OCLinEmig_OclFeatureDefinition> getOclinemig_oclfeaturedefinitions() {
        return oclinemig_oclfeaturedefinitions;
    }

    public void addOclinemig_oclfeaturedefinition(Oclinemig_oclfeaturedefinition oclinemig_oclfeaturedefinition) {
        this.oclinemig_oclfeaturedefinitions.add(oclinemig_oclfeaturedefinition);
    }

}