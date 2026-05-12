





import java.util.List;
import java.util.ArrayList;

public class HSM_RootFolder  {

    private String name;





    private List<OrState> orstates;


    public HSM_RootFolder(
        String name    ) {
        this.name = name;
        this.orstates = new ArrayList<>();
    }

    public HSM_RootFolder(
        String name        ArrayList<OrState> orstates    ) {
        this.name = name;
        this.orstates = orstates;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<OrState> getOrstates() {
        return orstates;
    }

    public void addOrstate(Orstate orstate) {
        this.orstates.add(orstate);
    }

}