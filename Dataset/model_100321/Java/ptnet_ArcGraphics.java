





import java.util.List;
import java.util.ArrayList;

public class ptnet_ArcGraphics extends Graphics {






    private ptnet_Position ptnet_position;




    private List<ptnet_Position> ptnet_positions;


    public ptnet_ArcGraphics(
    ) {
        super(
        );
        this.ptnet_positions = new ArrayList<>();
    }

    public ptnet_ArcGraphics(
        ArrayList<ptnet_Position> ptnet_positions    ) {
        this.ptnet_positions = ptnet_positions;
    }


    public ptnet_Position getPtnet_position() {
        return ptnet_position;
    }

    public void setPtnet_position(ptnet_Position ptnet_position) {
        this.ptnet_position = ptnet_position;
    }
    public List<ptnet_Position> getPtnet_positions() {
        return ptnet_positions;
    }

    public void addPtnet_position(Ptnet_position ptnet_position) {
        this.ptnet_positions.add(ptnet_position);
    }

}