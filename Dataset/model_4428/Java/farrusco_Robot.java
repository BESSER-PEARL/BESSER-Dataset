





import java.util.List;
import java.util.ArrayList;

public class farrusco_Robot  {

    private String Name;





    private List<farrusco_Filho> farrusco_filhos;




    private List<farrusco_Node> farrusco_nodes;




    private List<farrusco_Irmao> farrusco_irmaos;


    public farrusco_Robot(
        String Name    ) {
        this.Name = Name;
        this.farrusco_filhos = new ArrayList<>();
        this.farrusco_nodes = new ArrayList<>();
        this.farrusco_irmaos = new ArrayList<>();
    }

    public farrusco_Robot(
        String Name        ArrayList<farrusco_Filho> farrusco_filhos,        ArrayList<farrusco_Node> farrusco_nodes,        ArrayList<farrusco_Irmao> farrusco_irmaos    ) {
        this.Name = Name;
        this.farrusco_filhos = farrusco_filhos;
        this.farrusco_nodes = farrusco_nodes;
        this.farrusco_irmaos = farrusco_irmaos;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<farrusco_Filho> getFarrusco_filhos() {
        return farrusco_filhos;
    }

    public void addFarrusco_filho(Farrusco_filho farrusco_filho) {
        this.farrusco_filhos.add(farrusco_filho);
    }
    public List<farrusco_Node> getFarrusco_nodes() {
        return farrusco_nodes;
    }

    public void addFarrusco_node(Farrusco_node farrusco_node) {
        this.farrusco_nodes.add(farrusco_node);
    }
    public List<farrusco_Irmao> getFarrusco_irmaos() {
        return farrusco_irmaos;
    }

    public void addFarrusco_irmao(Farrusco_irmao farrusco_irmao) {
        this.farrusco_irmaos.add(farrusco_irmao);
    }

}