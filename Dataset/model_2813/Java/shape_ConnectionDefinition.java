





import java.util.List;
import java.util.ArrayList;

public class shape_ConnectionDefinition extends ShapeContainerElement {

    private String connectionStyle;



    public shape_ConnectionDefinition(
        String connectionStyle    ) {
        super(
        );
        this.connectionStyle = connectionStyle;
    }


    public String getConnectionstyle() {
        return connectionStyle;
    }

    public void setConnectionstyle(String connectionStyle) {
        this.connectionStyle = connectionStyle;
    }


}