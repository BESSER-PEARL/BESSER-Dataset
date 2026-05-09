





import java.util.List;
import java.util.ArrayList;

public class easyflow_Workflow  {

    private String dag;
    private String name;
    private String graph;
    private String jobDag;



    public easyflow_Workflow(
        String dag,        String name,        String graph,        String jobDag    ) {
        this.dag = dag;
        this.name = name;
        this.graph = graph;
        this.jobDag = jobDag;
    }


    public String getDag() {
        return dag;
    }

    public void setDag(String dag) {
        this.dag = dag;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getGraph() {
        return graph;
    }

    public void setGraph(String graph) {
        this.graph = graph;
    }
    public String getJobdag() {
        return jobDag;
    }

    public void setJobdag(String jobDag) {
        this.jobDag = jobDag;
    }


}