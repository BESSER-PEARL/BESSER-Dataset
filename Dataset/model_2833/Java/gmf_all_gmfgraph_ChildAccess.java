





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_ChildAccess  {

    private String accessor;





    private Figure figure;




    private FigureDescriptor figuredescriptor;


    public gmf_all_gmfgraph_ChildAccess(
        String accessor    ) {
        this.accessor = accessor;
    }


    public String getAccessor() {
        return accessor;
    }

    public void setAccessor(String accessor) {
        this.accessor = accessor;
    }

    public Figure getFigure() {
        return figure;
    }

    public void setFigure(Figure figure) {
        this.figure = figure;
    }
    public FigureDescriptor getFiguredescriptor() {
        return figuredescriptor;
    }

    public void setFiguredescriptor(FigureDescriptor figuredescriptor) {
        this.figuredescriptor = figuredescriptor;
    }

}