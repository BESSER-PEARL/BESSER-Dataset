





import java.util.List;
import java.util.ArrayList;

public class graphbt_Libraries  {






    private List<graphbt_Library> graphbt_librarys;


    public graphbt_Libraries(
    ) {
        this.graphbt_librarys = new ArrayList<>();
    }

    public graphbt_Libraries(
        ArrayList<graphbt_Library> graphbt_librarys    ) {
        this.graphbt_librarys = graphbt_librarys;
    }


    public List<graphbt_Library> getGraphbt_librarys() {
        return graphbt_librarys;
    }

    public void addGraphbt_library(Graphbt_library graphbt_library) {
        this.graphbt_librarys.add(graphbt_library);
    }

}