





import java.util.List;
import java.util.ArrayList;

public class out_RootContainer  {






    private List<out_RootOut> out_rootouts;


    public out_RootContainer(
    ) {
        this.out_rootouts = new ArrayList<>();
    }

    public out_RootContainer(
        ArrayList<out_RootOut> out_rootouts    ) {
        this.out_rootouts = out_rootouts;
    }


    public List<out_RootOut> getOut_rootouts() {
        return out_rootouts;
    }

    public void addOut_rootout(Out_rootout out_rootout) {
        this.out_rootouts.add(out_rootout);
    }

}