





import java.util.List;
import java.util.ArrayList;

public class scmodel_History extends State {

    private boolean shallow;



    public scmodel_History(
        boolean shallow    ) {
        super(
        );
        this.shallow = shallow;
    }


    public boolean getShallow() {
        return shallow;
    }

    public void setShallow(boolean shallow) {
        this.shallow = shallow;
    }


}