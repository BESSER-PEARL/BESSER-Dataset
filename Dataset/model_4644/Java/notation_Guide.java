





import java.util.List;
import java.util.ArrayList;

public class notation_Guide  {

    private int position;





    private notation_GuideStyle notation_guidestyle;




    private notation_GuideStyle notation_guidestyle;




    private List<notation_NodeEntry> notation_nodeentrys;


    public notation_Guide(
        int position    ) {
        this.position = position;
        this.notation_nodeentrys = new ArrayList<>();
    }

    public notation_Guide(
        int position        ArrayList<notation_NodeEntry> notation_nodeentrys    ) {
        this.position = position;
        this.notation_nodeentrys = notation_nodeentrys;
    }

    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }

    public notation_GuideStyle getNotation_guidestyle() {
        return notation_guidestyle;
    }

    public void setNotation_guidestyle(notation_GuideStyle notation_guidestyle) {
        this.notation_guidestyle = notation_guidestyle;
    }
    public notation_GuideStyle getNotation_guidestyle() {
        return notation_guidestyle;
    }

    public void setNotation_guidestyle(notation_GuideStyle notation_guidestyle) {
        this.notation_guidestyle = notation_guidestyle;
    }
    public List<notation_NodeEntry> getNotation_nodeentrys() {
        return notation_nodeentrys;
    }

    public void addNotation_nodeentry(Notation_nodeentry notation_nodeentry) {
        this.notation_nodeentrys.add(notation_nodeentry);
    }

}