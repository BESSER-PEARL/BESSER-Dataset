





import java.util.List;
import java.util.ArrayList;

public class SimplePDL_ResourceType extends ProcessElement {

    private int occurrences;
    private String name;





    private SimplePDL_Resource simplepdl_resource;


    public SimplePDL_ResourceType(
        int occurrences,        String name    ) {
        super(
        );
        this.occurrences = occurrences;
        this.name = name;
    }


    public int getOccurrences() {
        return occurrences;
    }

    public void setOccurrences(int occurrences) {
        this.occurrences = occurrences;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SimplePDL_Resource getSimplepdl_resource() {
        return simplepdl_resource;
    }

    public void setSimplepdl_resource(SimplePDL_Resource simplepdl_resource) {
        this.simplepdl_resource = simplepdl_resource;
    }

}