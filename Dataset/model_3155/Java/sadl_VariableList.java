





import java.util.List;
import java.util.ArrayList;

public class sadl_VariableList  {






    private List<sadl_ResourceName> sadl_resourcenames;




    private sadl_ExistentialNegation sadl_existentialnegation;


    public sadl_VariableList(
    ) {
        this.sadl_resourcenames = new ArrayList<>();
    }

    public sadl_VariableList(
        ArrayList<sadl_ResourceName> sadl_resourcenames    ) {
        this.sadl_resourcenames = sadl_resourcenames;
    }


    public List<sadl_ResourceName> getSadl_resourcenames() {
        return sadl_resourcenames;
    }

    public void addSadl_resourcename(Sadl_resourcename sadl_resourcename) {
        this.sadl_resourcenames.add(sadl_resourcename);
    }
    public sadl_ExistentialNegation getSadl_existentialnegation() {
        return sadl_existentialnegation;
    }

    public void setSadl_existentialnegation(sadl_ExistentialNegation sadl_existentialnegation) {
        this.sadl_existentialnegation = sadl_existentialnegation;
    }

}