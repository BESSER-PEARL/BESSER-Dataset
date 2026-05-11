





import java.util.List;
import java.util.ArrayList;

public class top_X extends WChild {






    private List<top_XChild> top_xchilds;


    public top_X(
    ) {
        super(
        );
        this.top_xchilds = new ArrayList<>();
    }

    public top_X(
        ArrayList<top_XChild> top_xchilds    ) {
        this.top_xchilds = top_xchilds;
    }


    public List<top_XChild> getTop_xchilds() {
        return top_xchilds;
    }

    public void addTop_xchild(Top_xchild top_xchild) {
        this.top_xchilds.add(top_xchild);
    }

}