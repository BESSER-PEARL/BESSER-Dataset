





import java.util.List;
import java.util.ArrayList;

public class cal_AstStructure  {






    private List<cal_AstConnection> cal_astconnections;




    private cal_AstNetwork cal_astnetwork;


    public cal_AstStructure(
    ) {
        this.cal_astconnections = new ArrayList<>();
    }

    public cal_AstStructure(
        ArrayList<cal_AstConnection> cal_astconnections    ) {
        this.cal_astconnections = cal_astconnections;
    }


    public List<cal_AstConnection> getCal_astconnections() {
        return cal_astconnections;
    }

    public void addCal_astconnection(Cal_astconnection cal_astconnection) {
        this.cal_astconnections.add(cal_astconnection);
    }
    public cal_AstNetwork getCal_astnetwork() {
        return cal_astnetwork;
    }

    public void setCal_astnetwork(cal_AstNetwork cal_astnetwork) {
        this.cal_astnetwork = cal_astnetwork;
    }

}