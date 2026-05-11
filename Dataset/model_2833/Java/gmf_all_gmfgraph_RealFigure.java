





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_RealFigure extends gmfgraph_CustomAttributeOwner, gmfgraph_AbstractFigure, gmfgraph_PinOwner {

    private String name;



    public gmf_all_gmfgraph_RealFigure(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}