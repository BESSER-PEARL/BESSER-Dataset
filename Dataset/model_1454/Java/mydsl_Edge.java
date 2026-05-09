





import java.util.List;
import java.util.ArrayList;

public class mydsl_Edge  {

    private String parsed_source;
    private String label;
    private String parsed_target;





    private mydsl_Graph mydsl_graph;


    public mydsl_Edge(
        String parsed_source,        String label,        String parsed_target    ) {
        this.parsed_source = parsed_source;
        this.label = label;
        this.parsed_target = parsed_target;
    }


    public String getParsed_source() {
        return parsed_source;
    }

    public void setParsed_source(String parsed_source) {
        this.parsed_source = parsed_source;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getParsed_target() {
        return parsed_target;
    }

    public void setParsed_target(String parsed_target) {
        this.parsed_target = parsed_target;
    }

    public mydsl_Graph getMydsl_graph() {
        return mydsl_graph;
    }

    public void setMydsl_graph(mydsl_Graph mydsl_graph) {
        this.mydsl_graph = mydsl_graph;
    }

}