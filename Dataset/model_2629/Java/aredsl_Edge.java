





import java.util.List;
import java.util.ArrayList;

public class aredsl_Edge  {

    private String originSemantics;
    private String description;
    private String destinationSemantics;
    private String id;





    private aredsl_Node aredsl_node;




    private aredsl_Node aredsl_node;


    public aredsl_Edge(
        String originSemantics,        String description,        String destinationSemantics,        String id    ) {
        this.originSemantics = originSemantics;
        this.description = description;
        this.destinationSemantics = destinationSemantics;
        this.id = id;
    }


    public String getOriginsemantics() {
        return originSemantics;
    }

    public void setOriginsemantics(String originSemantics) {
        this.originSemantics = originSemantics;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getDestinationsemantics() {
        return destinationSemantics;
    }

    public void setDestinationsemantics(String destinationSemantics) {
        this.destinationSemantics = destinationSemantics;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public aredsl_Node getAredsl_node() {
        return aredsl_node;
    }

    public void setAredsl_node(aredsl_Node aredsl_node) {
        this.aredsl_node = aredsl_node;
    }
    public aredsl_Node getAredsl_node() {
        return aredsl_node;
    }

    public void setAredsl_node(aredsl_Node aredsl_node) {
        this.aredsl_node = aredsl_node;
    }

}