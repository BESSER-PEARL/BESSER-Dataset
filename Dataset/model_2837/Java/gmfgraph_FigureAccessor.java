





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FigureAccessor extends FigureHandle {

    private String accessor;



    public gmfgraph_FigureAccessor(
        String accessor    ) {
        super(
        );
        this.accessor = accessor;
    }


    public String getAccessor() {
        return accessor;
    }

    public void setAccessor(String accessor) {
        this.accessor = accessor;
    }


}