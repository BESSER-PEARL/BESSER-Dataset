





import java.util.List;
import java.util.ArrayList;

public class easyflow_Workflow  {

    private String graph;
    private String name;
    private String jobDag;
    private String dag;



    public easyflow_Workflow(
        String graph,        String name,        String jobDag,        String dag    ) {
        this.graph = graph;
        this.name = name;
        this.jobDag = jobDag;
        this.dag = dag;
    }


    public String getGraph() {
        return graph;
    }

    public void setGraph(String graph) {
        this.graph = graph;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getJobdag() {
        return jobDag;
    }

    public void setJobdag(String jobDag) {
        this.jobDag = jobDag;
    }
    public String getDag() {
        return dag;
    }

    public void setDag(String dag) {
        this.dag = dag;
    }


}