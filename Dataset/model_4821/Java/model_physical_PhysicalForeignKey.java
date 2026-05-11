





import java.util.List;
import java.util.ArrayList;

public class model_physical_PhysicalForeignKey extends ModelObject {

    private String sourceName;
    private String destinationName;



    public model_physical_PhysicalForeignKey(
        String sourceName,        String destinationName    ) {
        super(
        );
        this.sourceName = sourceName;
        this.destinationName = destinationName;
    }


    public String getSourcename() {
        return sourceName;
    }

    public void setSourcename(String sourceName) {
        this.sourceName = sourceName;
    }
    public String getDestinationname() {
        return destinationName;
    }

    public void setDestinationname(String destinationName) {
        this.destinationName = destinationName;
    }


}